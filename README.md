# 🏥 SGHSS - Sistema de Gestão Hospitalar e de Serviços de Saúde

Backend API desenvolvido em Django REST Framework para o sistema de gestão hospitalar da instituição VidaPlus.

## 🚀 Tecnologias Utilizadas

- **Python 3.11**
- **Django 5.2**
- **Django REST Framework**
- **Simple JWT** (Autenticação)
- **DRF Spectacular** (Documentação Swagger)
- **PostgreSQL** (Pronto para produção)
- **SQLite** (Desenvolvimento)

  Funcionalidades  Implementadas
- **Autenticação JWT** com login por email
- **CRUD Completo** de Usuários, Pacientes, Médicos, Agendamentos e Prontuários
- **Sistema de Permissões** por tipo de usuário (Paciente, Médico, Admin)
- **Documentação Interativa** Swagger/OpenAPI
- **Painel Admin Django** customizado
- **Validações LGPD** para dados sensíveis

###  Endpoints Principais

| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| `POST` | `/api/token/` | Login JWT | Público |
| `GET` | `/api/usuarios/` | Listar usuários | Admin |
| `POST` | `/api/pacientes/` | Criar paciente | Admin |
| `GET` | `/api/medicos/` | Listar médicos | Público |
| `POST` | `/api/agendamentos/` | Criar agendamento | Paciente/Admin |
| `GET` | `/api/docs/` | Documentação Swagger | Público |

## 🛠️ Instalação e Execução

### Pré-requisitos
- Python 3.11+
- PostgreSQL (opcional para desenvolvimento)
- Git

### Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/RodrigoNPer/sghss-backend.git
   cd sghss-backend
Crie e ative um ambiente virtual

bash
python -m venv venv
# Linux/Mac:
source venv/bin/activate
# Windows:
.\venv\Scripts\activate
Instale as dependências

bash
pip install -r requirements.txt
Configure o banco de dados (SQLite já vem configurado)

bash
python manage.py migrate
Crie um superusuário

bash
python manage.py createsuperuser
Execute o servidor

bash
python manage.py runserver
Acesse a aplicação

API: http://localhost:8000/api/

Admin: http://localhost:8000/admin/

Documentação: http://localhost:8000/api/docs/

 Estrutura do Projeto
text
sghss-backend/
├── api/                 # Aplicação principal
│   ├── models.py       # Modelos de dados
│   ├── serializers.py  # Serializers da API
│   ├── views.py        # Views e endpoints
│   ├── urls.py         # URLs da aplicação
│   └── admin.py        # Painel admin
├── core/               # Configurações do projeto
│   ├── settings.py     # Configurações Django
│   └── urls.py         # URLs principais
├── requirements.txt    # Dependências
└── manage.py          # Script de gerenciamento
 Autenticação
A API usa JWT (JSON Web Tokens) para autenticação:

bash
# Obter token
POST /api/token/
{
    "email": "usuario@email.com",
    "password": "senha123"
}

# Usar token nas requisições
Authorization: Bearer <your_access_token>
Exemplos de Uso
Criar Paciente
bash
POST /api/pacientes/
{
    "usuario_id": "uuid-do-usuario",
    "convenio": "Unimed",
    "alergias": "Penicilina"
}
Criar Agendamento
bash
POST /api/agendamentos/
{
    "paciente_id": "uuid-do-paciente",
    "medico_id": "uuid-do-medico",
    "data_hora": "2025-08-30T10:00:00",
    "tipo": "presencial"
}




🔗 Links Úteis
Documentação Django - https://docs.djangoproject.com/en/5.2/

Django REST Framework - https://www.django-rest-framework.org/

Simple JWT - https://django-rest-framework-simplejwt.readthedocs.io/en/latest/
