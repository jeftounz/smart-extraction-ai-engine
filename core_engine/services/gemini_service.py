import os
import google.generativeai as genai
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

class GeminiService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("⚠️ Falta la GEMINI_API_KEY en el archivo .env")
        
        genai.configure(api_key=api_key)
        # Usamos el modelo Flash porque es rápido e ideal para procesar texto
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    def analyze_jobs(self, jobs_list):
        # Perfil base para el análisis de la IA
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
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Error conectando con Gemini: {e}"

if __name__ == "__main__":
    # Prueba rápida del módulo aislado
    dummy_data = [{'title': 'Full Stack Flutter Developer', 'company': 'Wellbeinn'}]
    ai = GeminiService()
    print("\n--- ANÁLISIS DE LA IA ---")
    print(ai.analyze_jobs(dummy_data))