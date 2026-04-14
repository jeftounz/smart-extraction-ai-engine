import threading
import json
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from core_engine.models import ScrapingJob, ScrapedData
from .serializers import ScrapingJobSerializer
from core_engine.scrapers.linkedin_scraper import LinkedInScraper
from core_engine.services.gemini_service import GeminiService

# ==========================================
# EL MOTOR EN SEGUNDO PLANO
# ==========================================
def run_scraping_engine(job_id):
    # 1. Recuperamos el trabajo de la base de datos
    job = ScrapingJob.objects.get(id=job_id)
    job.status = 'in_progress'
    job.save()

    print(f"⚙️ Motor Iniciado: Buscando '{job.name}'...")

    try:
        # 2. Encendemos Selenium (Usamos el nombre del job como palabra clave)
        keyword = job.name if job.name else "Developer"
        scraper = LinkedInScraper(keyword, "Remote")# Buscamos remoto por defecto
        extracted_jobs = scraper.run()

        if not extracted_jobs:
            job.status = 'failed'
            job.error_message = "No se encontraron vacantes para este perfil."
            job.save()
            return

        print(f"✅ Scraping completado. Evaluando {len(extracted_jobs)} vacantes con Gemini...")

        # 3. Encendemos la Inteligencia Artificial
        ai_service = GeminiService()

        # 4. Guardamos cada vacante en la Base de Datos con su análisis
        for data in extracted_jobs:
            # Le pedimos a Gemini que analice esta vacante en particular
            # (Convertimos el diccionario a string para la IA)
            ai_analysis = ai_service.analyze_jobs(str(data))

            # Creamos el registro en PostgreSQL
            ScrapedData.objects.create(
                job=job,
                title=data.get('title', 'Sin título'),
                company=data.get('company', 'Sin empresa'),
                link=data.get('link', ''),
                raw_content=json.dumps(data, ensure_ascii=False),
                processed_content=ai_analysis # 🧠 ¡Aquí guardamos el Tech Match!
            )

        # 5. Finalizamos el trabajo con éxito
        job.status = 'completed'
        job.save()
        print(f"🎉 Job '{job.name}' finalizado. Resultados guardados en PostgreSQL.")

    except Exception as e:
        job.status = 'failed'
        job.error_message = str(e)
        job.save()
        print(f"❌ Error en el motor: {e}")


# ==========================================
# LA VISTA DE LA API (DRF)
# ==========================================
class ScrapingJobListCreateView(generics.ListCreateAPIView):
    serializer_class = ScrapingJobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Solo devolvemos los trabajos del usuario autenticado
        return ScrapingJob.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Guardamos el registro inicial en la base de datos (Estado: Pendiente)
        job = serializer.save(user=self.request.user, status='pending')
        
        # Desencadenamos el motor de Scraping en un hilo paralelo
        thread = threading.Thread(target=run_scraping_engine, args=(job.id,))
        thread.start()