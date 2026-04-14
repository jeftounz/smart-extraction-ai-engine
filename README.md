# Smart Extraction AI Engine 🤖🔍

Professional web automation & data intelligence framework. Built with Python (OOP), Selenium, and Django REST Framework. Features semantic analysis via Gemini AI for strategic data processing, JWT Authentication, and PostgreSQL persistence.

---

## 🏢 Enterprise-Grade Web Automation & Data Intelligence Framework

This project is an advanced data extraction engine designed to overcome the limitations of traditional scraping. It integrates Artificial Intelligence (Gemini API) to transform unstructured web data into strategic insights and exposes its services through a secure and asynchronous RESTful API.

---

## 🎯 SMART Goals (Phase 1: MVP)

1. **S (Specific):** Develop a web engine that extracts tech job vacancies from **LinkedIn**, processes role requirements (e.g., Flutter Developer) with Gemini AI, and saves technical insights in PostgreSQL.
2. **M (Measurable):** Achieve an extraction success rate >90% by evading dynamic blocks and process HTTP requests in <100ms using background execution.
3. **A (Achievable):** Implement a modular architecture in Python using Selenium, Django REST Framework, and JSON Web Tokens (JWT).
4. **R (Relevant):** Demonstrate engineering skills in Backend development, secure API design, automation, and Generative AI adoption.
5. **T (Time-bound):** Deliver the functional core of the engine (Core Engine + Auth + AI) in 3 weeks.

---

## 🏗️ System Architecture

The system follows **Clean Architecture**, **OOP** principles, and non-blocking API design:

* **Security & Auth Layer:** Identity management (Custom User) and endpoint protection via JSON Web Tokens (JWT). Strict data isolation per user.
* **API & Orchestration Layer:** Endpoints built with Django REST Framework (DRF) that receive requests and delegate heavy processing to background threads (`threading`), guaranteeing instant responses (`201 Created` / `Status: Pending`).
* **Scraping Layer:** Chromium driver management and background bot detection evasion.
* **Intelligence Layer:** Natural Language Processing (NLP) pipeline via Gemini API for categorization, technical 'Skill Gaps' analysis, and 'Tech Match' validation.
* **Storage Layer:** Relational persistence (One-to-Many) in PostgreSQL.

---

## 🔌 API Endpoints (Core Modules)

**1. Authentication Module (JWT)**
* `POST /api/auth/login/` - Obtains `access_token` and `refresh_token`.
* `POST /api/auth/token/refresh/` - Renews the access token.

**2. Extraction & AI Module (Protected)**
* `POST /api/jobs/` - Creates an asynchronous extraction job. Triggers Selenium and Gemini in the background.
* `GET /api/jobs/` - Retrieves the authenticated user's job history, including nested semantic AI analysis.

---

## 🛠️ Tech Stack

* **Language:** Python 3.12+ (OOP)
* **Backend & API:** Django, Django REST Framework, SimpleJWT
* **Automation:** Selenium & BeautifulSoup4
* **AI:** Gemini API (Google Generative AI)
* **Database:** PostgreSQL & Psycopg2
* **Infrastructure:** Multithreading (Asynchrony in DRF), Docker & Docker Compose (Coming soon)

---

## 📂 Project Structure

```text
smart-extraction-ai-engine/
├── config/                # Main router and Django configuration
└── core_engine/           # Main application
    ├── api/               # DRF Views, Serializers, and isolated URLs
    ├── management/        # CLI commands for local testing
    ├── scrapers/          # Extraction logic (LinkedInScraper)
    ├── services/          # AI Integration (GeminiService)
    ├── utils/             # Cross-cutting helpers and utilities
    └── models.py          # Relational DB Schemas (CustomUser, ScrapingJob, ScrapedData)