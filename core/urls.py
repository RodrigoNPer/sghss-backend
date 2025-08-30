from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenRefreshView
from api.views import CustomTokenObtainPairView

# Personaliza o título do Admin
admin.site.site_header = "Sistema de Gestão Hospitalar e de Serviços de Saúde (SGHSS) Vidaplus"
admin.site.site_title = "SGHSS Admin"
admin.site.index_title = "Administração do SGHSS"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]