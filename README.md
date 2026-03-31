# Smart Extraction AI Engine 🤖🔍

Professional web automation & data intelligence framework. Built with Python (OOP), Selenium, and Django REST Framework. Features semantic analysis via Gemini AI for strategic data processing and PostgreSQL persistence.

---

## 🏢 Enterprise-Grade Web Automation & Data Intelligence Framework

Este proyecto es un motor avanzado de extracción de datos diseñado para superar las limitaciones del scraping tradicional, integrando Inteligencia Artificial (Gemini API) para transformar datos web no estructurados en información estratégica.

---

## 🎯 Objetivos SMART (Fase 1: MVP)

1.  **S (Específico):** Desarrollar un motor que extraiga vacantes tecnológicas de **LinkedIn**, procese los requisitos de roles (ej. Flutter Developer) con Gemini AI y los guarde en PostgreSQL.
2.  **M (Medible):** Lograr una tasa de éxito de extracción >90% evadiendo bloqueos dinámicos.
3.  **A (Alcanzable):** Implementar una arquitectura modular en Python utilizando Selenium (Modo Stealth) y Django REST Framework.
4.  **R (Relevante):** Demostrar habilidades de ingeniería en automatización, IA Generativa y diseño de sistemas escalables.
5.  **T (Tiempo):** Entregar el núcleo funcional del motor en 3 semanas.

---

## 🏗️ Arquitectura del Sistema

El sistema sigue los principios de **Clean Architecture** y **POO**:

* **Scraping Layer:** Gestión de drivers de Chromium, rotación de agentes y evasión de detección de bots mediante `selenium-stealth`.
* **Intelligence Layer:** Pipeline de procesamiento de lenguaje natural (NLP) mediante Gemini API para categorización, análisis de 'Skill Gaps' y limpieza de datos.
* **Storage & API Layer:** Persistencia en PostgreSQL y exposición de datos mediante Django REST Framework (DRF).

---

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.12+ (OOP)
* **Automatización:** Selenium & BeautifulSoup4
* **Backend:** Django & Django REST Framework
* **IA:** Gemini API (Google Generative AI)
* **Base de Datos:** PostgreSQL
* **Infraestructura:** Docker & Docker Compose (Próximamente)

---

## 📂 Estructura del Proyecto

```text
smart-extraction-ai-engine/
├── config/                # Configuración global de Django
└── core_engine/           # Aplicación principal
    ├── api/               # Endpoints RESTful y Serializadores
    ├── management/        # Comandos CLI (Motor de ejecución)
    ├── scrapers/          # Lógica de extracción automatizada
    ├── services/          # Integración con servicios externos (Gemini AI)
    ├── utils/             # Helpers y utilidades transversales
    └── models.py          # Esquemas de Base de Datos