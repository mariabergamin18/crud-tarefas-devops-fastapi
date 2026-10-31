""" DevOps """

from datetime import datetime, timezone
from typing import Annotated, List
import os

from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Session, create_engine, select
from requests.exceptions import ConnectionError as RequestConnectionError

from .modelo import Tarefa

DATABASE_USERNAME = os.environ.get("DATABASE_USERNAME")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
DATABASE_ADDRESS = os.environ.get("DATABASE_ADDRESS")
DATABASE = os.environ.get("DATABASE")

if DATABASE_USERNAME is None:
    print("DATABASE_USERNAME está faltando")
    exit(1)

if DATABASE_PASSWORD is None:
    print("DATABASE_PASSWORD está faltando")
    exit(1)

if DATABASE_ADDRESS is None:
    print("DATABASE_ADDRESS está faltando")
    exit(1)

if DATABASE is None:
    print("DATABASE está faltando")
    exit(1)

ENGINE = create_engine(f"mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_ADDRESS}:3306/{DATABASE}")

def criar_sessao():
    """ sessão """
    with Session(ENGINE) as s:
        yield s

SESSAO = Annotated[Session, Depends(criar_sessao)]

async def inicializacao(api: FastAPI):
    """Engine = banco de dados, inicializa tabela"""
    SQLModel.metadata.create_all(ENGINE)
    yield

APP = FastAPI(lifespan=inicializacao)
TAREFAS = []

# GET /tarefas: Lista todas as tarefas (somente id e titulo)
@APP.get("/tarefas")
async def tarefas(sessao: SESSAO) -> List[Tarefa]:
    """ Descrição """

    #retorna sequencia das tarefas
    lista_tarefas = sessao.exec(select(Tarefa).offset(0)).all()

    return lista_tarefas


# POST /tarefas: Cria tarefa
@APP.post("/tarefas", status_code=201)
async def post_tarefa(sessao: SESSAO, titulo: str, descricao: str = None):
    """ Descrição """
    tarefa_nova = Tarefa(
        titulo=titulo, 
        descricao=descricao, 
        data_criacao=datetime.now().astimezone(timezone.utc),
        )

    sessao.add(tarefa_nova)
    sessao.commit()
    sessao.refresh(tarefa_nova)

    return {"mensagem": "OK"}

# GET /tarefas/{id_tarefa}: Visualizar tarefa específica
@APP.get("/tarefas/{id_tarefa}")
async def tarefa_especifica(sessao: SESSAO, id_tarefa: int) -> Tarefa:
    """ Descrição """
    # select * from tarefas where id == id_tarefa
    regra = select(Tarefa).where(Tarefa.id == id_tarefa)
    resultado = sessao.exec(regra).all()

    if resultado:
        return resultado[0]

    return {"mensagem": "Tarefa não existe"}

# PUT /tarefas/{id}: Atualiza tarefa específica
@APP.put("/tarefas/{id_tarefa}")
async def concluir_tarefa(sessao: SESSAO, id_tarefa: int):
    """ Descrição """
    regra = select(Tarefa).where(Tarefa.id == id_tarefa)
    resultado = sessao.exec(regra).all()

    if not resultado:
        return {"mensagem": "Tarefa não existe"}

    if resultado[0].concluida is True:
        return {"mensagem": "Tarefa já finalizada"}

    resultado[0].finalizar()

    sessao.add(resultado[0])
    sessao.commit()
    sessao.refresh(resultado[0])

    return {"mensagem": "Tarefa atualizada"}
       

# DELETE /tarefas/{id_tarefa}: Exclui tarefa
@APP.delete("/tarefas/{id_tarefa}")
async def apagar_tarefa(sessao: SESSAO, id_tarefa: int):
    """Rota para apagar tarefa."""

    regra = select(Tarefa).where(Tarefa.id == id_tarefa)
    resultado = sessao.exec(regra).all()
    
    if not resultado:
        return {"mensagem": "Tarefa não existe"}    

    tarefa = resultado[0]

    sessao.delete(tarefa)
    sessao.commit()

    return {"mensagem": "Tarefa removida"}

@APP.get("/")
async def index():
    """ Descrição """
    return {"mensagem": "Olá, mundo!"}

@APP.get("/autor")
async def mostrar_autor():
    """ Mostra nome do autor """
    return {"mensagem": "maria eduarda bergamin jorge"}
