from django.urls import path
from .views import ScrapingJobListCreateView

urlpatterns = [
    # Mapea a: GET /api/jobs/ y POST /api/jobs/
    path('jobs/', ScrapingJobListCreateView.as_view(), name='job-list-create'),
]