from django.contrib import admin
from .models import Usuario, Paciente, Medico, Agendamento, Prontuario

# Personaliza os nomes exibidos no Admin
admin.site.site_header = "Sistema de Gestão Hospitalar e de Serviços de Saúde (SGHSS)"
admin.site.site_title = "SGHSS Admin Portal"
admin.site.index_title = "Bem-vindo ao Portal de Administração do SGHSS"

# Registre seus modelos aqui
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'tipo', 'cpf')
    list_filter = ('tipo', 'data_criacao')
    search_fields = ('email', 'first_name', 'last_name', 'cpf')

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'convenio')
    search_fields = ('usuario__email', 'usuario__first_name', 'usuario__last_name')

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'crm', 'especialidade', 'valor_consulta')
    list_filter = ('especialidade',)
    search_fields = ('usuario__email', 'usuario__first_name', 'usuario__last_name', 'crm')

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'data_hora', 'tipo', 'status')
    list_filter = ('status', 'tipo', 'data_hora')
    date_hierarchy = 'data_hora'

@admin.register(Prontuario)
class ProntuarioAdmin(admin.ModelAdmin):
    list_display = ('agendamento', 'data_criacao')
    list_filter = ('data_criacao',)