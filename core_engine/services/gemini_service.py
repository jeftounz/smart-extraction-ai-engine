import os
from google import genai # <--- Nueva importación
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

class GeminiService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("⚠️ Falta la GEMINI_API_KEY en el archivo .env")
        
        # Inicializamos el nuevo Cliente Oficial
        self.client = genai.Client(api_key=api_key)

    def analyze_jobs(self, jobs_list):
        my_profile = """
        - Ingeniero de Sistemas
        - Experiencia en desarrollo móvil con Flutter
        - Especialista en Tecnología (CRM como Vtiger)
        - Automatización de procesos (Make.com)
        - Lenguajes: Python, aprendiendo Node.js
        - Entorno: Ubuntu/Linux
        """

        prompt = f"""
        Actúa como un Tech Recruiter Senior.
        Aquí tienes mi perfil técnico actual:
        {my_profile}

        Y aquí tienes una lista de vacantes extraídas hoy de LinkedIn:
        {jobs_list}

        Haz un análisis rápido y dime:
        1. ¿Cuál de estas vacantes es el mejor 'match' para mi perfil y por qué?
        2. ¿Qué 'Skill Gap' (habilidad faltante) notas en el mercado actual para estos puestos de Flutter que yo debería priorizar estudiar?
        
        Responde en español, de forma muy concisa y directa al grano.
        """

        try:
            print("🤖 Procesando análisis semántico con Gemini...")
            # Nueva forma de generar contenido según la documentación 2024/2025
            response = self.client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"❌ Error conectando con Gemini: {e}"