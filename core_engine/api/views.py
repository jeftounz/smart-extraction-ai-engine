from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from core_engine.models import ScrapingJob
from .serializers import ScrapingJobSerializer

class ScrapingJobListCreateView(generics.ListCreateAPIView):
    serializer_class = ScrapingJobSerializer
    permission_classes = [IsAuthenticated] # Exige que el JWT vaya en los Headers

    def get_queryset(self):
        # Filtro de seguridad: Solo devolvemos los jobs del usuario que hace la petición
        return ScrapingJob.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Al hacer POST, guardamos el Job asociándolo automáticamente al usuario autenticado
        job = serializer.save(user=self.request.user, status='pending')
        
        # TODO: Aquí es donde "despertaremos" a Selenium y Gemini en el próximo paso
        print(f"🚀 Nuevo Job creado: {job.name} por {job.user.username}")