from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import UserManager
import uuid

# Modelo customizado de Usuário que servirá como base para Paciente e Medico
class Usuario(AbstractUser):
    TIPOS_USUARIO = (
        ('paciente', 'Paciente'),
        ('medico', 'Médico'),
        ('admin', 'Administrador'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # SOBRESCREVE o campo email para ser único
    email = models.EmailField(unique=True, verbose_name='email address')
    tipo = models.CharField(max_length=10, choices=TIPOS_USUARIO, default='paciente')
    cpf = models.CharField(max_length=11, unique=True, validators=[MinLengthValidator(11)])
    telefone = models.CharField(max_length=15, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    # Substitui o username padrão pelo email para login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'cpf']  # Campos obrigatórios ao criar superuser
    
    objects = UserManager()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_tipo_display()})"

class Paciente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    convenio = models.CharField(max_length=100, blank=True, null=True)
    alergias = models.TextField(blank=True, null=True)
    medicamentos_uso_continuo = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
    
    def __str__(self):
        return f"Paciente: {self.usuario.first_name} {self.usuario.last_name}"

class Medico(models.Model):
    ESPECIALIDADES = (
        ('cardiologia', 'Cardiologia'),
        ('dermatologia', 'Dermatologia'),
        ('ortopedia', 'Ortopedia'),
        ('pediatria', 'Pediatria'),
        ('clinico_geral', 'Clínico Geral'),
        ('ginecologia', 'Ginecologia'),
    )
    
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    crm = models.CharField(max_length=20, unique=True)
    especialidade = models.CharField(max_length=20, choices=ESPECIALIDADES)
    valor_consulta = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'
    
    def __str__(self):
        return f"Dr. {self.usuario.first_name} {self.usuario.last_name} - {self.get_especialidade_display()}"

class Agendamento(models.Model):
    STATUS_CHOICES = (
        ('agendado', 'Agendado'),
        ('realizado', 'Realizado'),
        ('cancelado', 'Cancelado'),
        ('nao_compareceu', 'Não Compareceu'),
    )
    
    TIPO_CONSULTA = (
        ('presencial', 'Presencial'),
        ('online', 'Online'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='agendamentos')
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='agendamentos')
    data_hora = models.DateTimeField()
    tipo = models.CharField(max_length=10, choices=TIPO_CONSULTA, default='presencial')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='agendado')
    observacoes = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        ordering = ['-data_hora']
    
    def __str__(self):
        return f"Consulta {self.paciente} com {self.medico} - {self.data_hora}"

class Prontuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    agendamento = models.OneToOneField(Agendamento, on_delete=models.CASCADE, related_name='prontuario')
    anotacoes = models.TextField()
    prescricao = models.TextField(blank=True, null=True)
    diagnosticos = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Prontuário'
        verbose_name_plural = 'Prontuários'
    
    def __str__(self):
        return f"Prontuário {self.agendamento.paciente} - {self.agendamento.data_hora.date()}"