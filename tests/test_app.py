from fastapi.testclient import TestClient
from app import APP
from datetime import datetime

CLIENT = TestClient(APP)
DATA = None
DATA_CONCLUSAO = None

def test_index():
    resposta = CLIENT.get("/")
    assert resposta.status_code == 200
    assert resposta.json() == {"mensagem": "Olá, mundo!"}

def test_tarefas_get():
    resposta = CLIENT.get("/tarefas")
    assert resposta.status_code == 200

    # Testando se a rota retorna uma lista vazia
    assert resposta.json() == []

def test_tarefas_post():
    global DATA
    resposta = CLIENT.post("/tarefas?titulo=teste&descricao=teste")
    DATA = datetime.now().isoformat(timespec="seconds")

    assert resposta.status_code == 201
    assert resposta.json() == {"mensagem": "OK"}

    resposta = CLIENT.get("/tarefas")
    assert resposta.json() == [
        {"0": "teste"}
    ]

def test_tarefa_criada():
    resposta = CLIENT.get("/tarefas/0")
    assert resposta.status_code == 200
    assert resposta.json() == {
        "id": 0,
        "titulo": "teste",
        "descricao": "teste",
        "concluida": False,
        "criada_em": str(DATA),
    }

def test_tarefas_put():
    global DATA_CONCLUSAO
    resposta = CLIENT.put("/tarefas/0")
    DATA_CONCLUSAO = datetime.now().isoformat(timespec="seconds")
    assert resposta.json() == {"mensagem": "Tarefa atualizada"}

    resposta = CLIENT.put("/tarefas/1")
    assert resposta.json() == {"mensagem": "Tarefa não existe"}

def test_tarefas_get_id():
    resposta = CLIENT.get("/tarefas/0")
    assert resposta.status_code == 200
    assert resposta.json() == {
        "id": 0,
        "titulo": "teste",
        "descricao": "teste",
        "concluida": True,
        "criada_em": str(DATA),
        "concluida_em": str(DATA_CONCLUSAO)
    }

    resposta = CLIENT.get("/tarefas/1")
    assert resposta.json() == {"mensagem": "Tarefa não existe"}

def teste_tarefas_delete():
    resposta = CLIENT.delete("/tarefas/1")
    assert resposta.json() == {"mensagem": "Tarefa não existe"}

    resposta = CLIENT.delete("/tarefas/0")
    assert resposta.json() == {"mensagem": "Tarefa apagada"} 

    resposta = CLIENT.get("/tarefas")
    assert resposta.json() == []

def teste_autor():
    resposta = CLIENT.get("/autor")
    assert resposta.status_code == 200
    assert resposta.json() == {"mensagem": "maria eduarda bergamin jorge"}