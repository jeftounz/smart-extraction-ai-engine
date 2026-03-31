from django.db import models
from django.contrib.auth.models import AbstractUser

# ==========================================
# MÓDULO 1: AUTENTICACIÓN Y USUARIOS
# ==========================================
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('personal', 'Personal'),
        ('business', 'Business'),
    ]
    
    # Campos extraídos de tu diagrama SaaS
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='personal')
    company_name = models.CharField(max_length=255, blank=True, null=True)
    api_access = models.BooleanField(default=True)
    
    # Adaptamos 'deepseek_access' a un nombre agnóstico para IA
    ai_access = models.BooleanField(default=True) 

    def __str__(self):
        return self.username

# ==========================================
# MÓDULO 2: MOTOR DE SCRAPING
# ==========================================
class ScrapingJob(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    # Relación fundamental: Un usuario tiene muchos Jobs
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='scraping_jobs')
    name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Adaptamos 'deepseek_prompt' de tu diseño
    ai_prompt = models.TextField(blank=True, null=True) 
    error_message = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Job #{self.id} - {self.name} ({self.status})"

class ScrapedData(models.Model):
    # Relación: Un Job tiene mucha data extraída
    job = models.ForeignKey(ScrapingJob, on_delete=models.CASCADE, related_name='scraped_data')
    
    # Campos específicos de nuestra extracción de LinkedIn
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    link = models.URLField(max_length=800)
    
    # Del diagrama: raw_content y processed_content
    raw_content = models.TextField(blank=True, null=True)
    processed_content = models.TextField(blank=True, null=True) # Aquí irá el análisis de Gemini
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} en {self.company}"