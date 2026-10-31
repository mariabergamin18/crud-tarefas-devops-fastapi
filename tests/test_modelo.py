from datetime import datetime
from app.modelo import Tarefa

def criar_tarefa_exemplo():
    return Tarefa(id=0, titulo="Teste", data_criacao=datetime.now().isoformat(timespec='seconds'))

def test_nova_tarefa():
    """ teste """
    t = criar_tarefa_exemplo()

    assert t.id == 0
    assert t.titulo == "Teste"
    assert t.descricao == None
    assert t.data_criacao.isoformat() == datetime.now().isoformat(timespec='seconds')
    assert t.data_conclusao == None
    assert t.concluida == False

def test_tarefa_concluida():
    """ verificar se a tarefa foi concluida"""
    t = criar_tarefa_exemplo()

    t.finalizar()
    assert t.concluida == True
    assert t.data_conclusao == datetime.now().isoformat(timespec='seconds')