from django.core.management.base import BaseCommand
from core_engine.scrapers.linkedin_scraper import LinkedInScraper
from core_engine.services.gemini_service import GeminiService
import json

class Command(BaseCommand):
    help = 'Ejecuta el scraper de LinkedIn y analiza los resultados con Gemini AI'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('🚀 Iniciando el Motor de Extracción...'))

        # Fase 1: Extracción
        self.stdout.write(self.style.WARNING('🔍 Buscando vacantes de Flutter en LinkedIn...'))
        scraper = LinkedInScraper("Flutter Developer", "Spain")
        jobs_data = scraper.run()

        if not jobs_data:
            self.stdout.write(self.style.ERROR('❌ No se extrajeron datos. Revisa tu conexión o selectores.'))
            return

        self.stdout.write(self.style.SUCCESS(f'✅ Extracción completada: {len(jobs_data)} empleos obtenidos.'))

        # Fase 2: Análisis de Inteligencia Artificial
        self.stdout.write(self.style.WARNING('🤖 Enviando datos crudos a Gemini para análisis semántico...'))
        ai_service = GeminiService()
        
        # Convertimos la lista de diccionarios a texto formateado para la IA
        jobs_text = json.dumps(jobs_data, indent=2, ensure_ascii=False)
        analysis = ai_service.analyze_jobs(jobs_text)

        # Fase 3: Mostrar el Reporte Final
        self.stdout.write(self.style.SUCCESS('\n' + '='*40))
        self.stdout.write(self.style.SUCCESS('🧠 REPORTE DE IA - TECH MATCH 🧠'))
        self.stdout.write(self.style.SUCCESS('='*40 + '\n'))
        
        # Imprimimos la respuesta tal cual nos la da Gemini
        print(analysis)
        
        self.stdout.write(self.style.SUCCESS('\n✨ Proceso finalizado con éxito.'))