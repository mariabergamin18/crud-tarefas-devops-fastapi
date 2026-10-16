from fastapi import FastAPI
from datetime import datetime

#ESTRUTURA DA TAREFA
"""
{
"id" -> int,
"titulo" -> str
"descricao" -> str
"concluida" -> bool
"criado_em" -> datetime
}
"""

APP = FastAPI()
TAREFAS = []


def criar_tarefa(titulo, descricao):
    return {
        "id": len(TAREFAS),
        "titulo": titulo,
        "descricao": descricao,
        "concluida": False,
        "criada_em": datetime.now()
    }

# criando rota /tarefas
@APP.get("/tarefas")
async def tarefas():
    return TAREFAS

# criando post para criar tarefa
@APP.post("/tarefas")
async def post_tarefa(titulo: str, descricao: str):
    global TAREFAS
    
    tarefanova = criar_tarefa(titulo, descricao)

    TAREFAS.append(tarefanova)
    
    return {"mensagem":"Tarefa criada"}

# criando rota de api para o caminho raiz do app
@APP.get("/")
async def index():
    return {"mensagem": "Olá, mundo!"}