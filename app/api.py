from psutil import users
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from BaseModels import UserBaseModels
from Repository import SchedulesRepository, UserRepository

# Requisitos: baixar MongoDb community para rodar o banco em localhost por enqaunto, depois podemos colocar em nuvem
# O banco (schedule) tem 2 'folders' de dados
# O primeiro guarda email e senha para autenticaçao de usuários (user_credentials)
# O segundo guarda dados de agendamentos dos usuários (user_schedules)

api = FastAPI()

# Cadastra novo usuário no sistema
@api.post("/create-user", status_code=200, tags=["users"])
async def create_user(request: UserBaseModels.User):
    return UserRepository.Create(request)

# Retorna uma lista de dicionários, cada dicionário possui o email de um usuário e seus agendametos
@api.get("C", status_code=200, tags=["schedules"])
async def list_all_schedules():
    return SchedulesRepository.ListAllShedules()

# Autenticação de um usuário para login
@api.post("/login", status_code=200, tags=["users"])
async def login_user(request: UserBaseModels.User):
    return UserRepository.Authorization(request.email, request.password)

# Insere um novo agendamento
@api.put("/create-schedule", status_code=200, tags=["schedules"])
async def create_schedule(request: UserBaseModels.User_Schedule):
    return SchedulesRepository.Create(request)

# Busca um usuário específico atraves de um email
@api.get("/{email}", status_code=200, tags=["schedules"])
async def get_schedules_by_email(email):
    return SchedulesRepository.GetSchedulesByEmail(email)