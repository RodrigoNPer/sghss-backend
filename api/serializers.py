from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Usuario, Paciente, Medico, Agendamento, Prontuario

# Serializer customizado para autenticação JWT com email
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'  # Define que o campo de login é 'email'

    def validate(self, attrs):
        # Personaliza a mensagem de erro para email
        try:
            return super().validate(attrs)
        except Exception as e:
            raise serializers.ValidationError({
                'email': 'Email ou senha incorretos.'
            })

# Serializers para os modelos
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

class PacienteSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)  # Para leitura
    usuario_id = serializers.UUIDField(write_only=True)  # Para escrita
    
    class Meta:
        model = Paciente
        fields = '__all__'
    
    def create(self, validated_data):
        # Extrai o ID do usuário
        usuario_id = validated_data.pop('usuario_id')
        # Obtém a instância do usuário
        usuario = Usuario.objects.get(id=usuario_id)
        # Cria o paciente vinculado ao usuário
        paciente = Paciente.objects.create(usuario=usuario, **validated_data)
        return paciente

class MedicoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)  # Para leitura
    usuario_id = serializers.UUIDField(write_only=True)  # Para escrita
    
    class Meta:
        model = Medico
        fields = '__all__'
    
    def create(self, validated_data):
        # Extrai o ID do usuário
        usuario_id = validated_data.pop('usuario_id')
        # Obtém a instância do usuário
        usuario = Usuario.objects.get(id=usuario_id)
        # Cria o médico vinculado ao usuário
        medico = Medico.objects.create(usuario=usuario, **validated_data)
        return medico

class AgendamentoSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer(read_only=True)
    medico = MedicoSerializer(read_only=True)
    paciente_id = serializers.UUIDField(write_only=True)  # Para escrita
    medico_id = serializers.UUIDField(write_only=True)    # Para escrita
    
    class Meta:
        model = Agendamento
        fields = '__all__'
    
    def create(self, validated_data):
        # Extrai os IDs
        paciente_id = validated_data.pop('paciente_id')
        medico_id = validated_data.pop('medico_id')
        # Obtém as instâncias
        paciente = Paciente.objects.get(id=paciente_id)
        medico = Medico.objects.get(id=medico_id)
        # Cria o agendamento
        agendamento = Agendamento.objects.create(
            paciente=paciente, 
            medico=medico, 
            **validated_data
        )
        return agendamento

class ProntuarioSerializer(serializers.ModelSerializer):
    agendamento = AgendamentoSerializer(read_only=True)
    agendamento_id = serializers.UUIDField(write_only=True)  # Para escrita
    
    class Meta:
        model = Prontuario
        fields = '__all__'
    
    def create(self, validated_data):
        # Extrai o ID do agendamento
        agendamento_id = validated_data.pop('agendamento_id')
        # Obtém a instância do agendamento
        agendamento = Agendamento.objects.get(id=agendamento_id)
        # Cria o prontuário
        prontuario = Prontuario.objects.create(
            agendamento=agendamento, 
            **validated_data
        )
        return prontuario