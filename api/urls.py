from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UsuarioViewSet, PacienteViewSet, MedicoViewSet, 
    AgendamentoViewSet, ProntuarioViewSet
)

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'agendamentos', AgendamentoViewSet)
router.register(r'prontuarios', ProntuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]