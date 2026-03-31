from django.contrib import admin
from django.urls import path, include # <--- Asegúrate de importar 'include'
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Módulo de Autenticación JWT
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Módulo de API Core (Jobs y Resultados)
    path('api/', include('core_engine.api.urls')), # <--- Conecta nuestras nuevas rutas
]