from rest_framework import serializers
from core_engine.models import ScrapingJob, ScrapedData

class ScrapedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedData
        fields = ['id', 'title', 'company', 'link', 'processed_content', 'created_at']

class ScrapingJobSerializer(serializers.ModelSerializer):
    # Anidamos los resultados para que el frontend reciba todo en una sola petición
    scraped_data = ScrapedDataSerializer(many=True, read_only=True)

    class Meta:
        model = ScrapingJob
        fields = ['id', 'name', 'status', 'ai_prompt', 'error_message', 'created_at', 'scraped_data']
        # Protegemos estos campos para que el usuario no los altere manualmente al crear el Job
        read_only_fields = ['status', 'error_message', 'created_at']