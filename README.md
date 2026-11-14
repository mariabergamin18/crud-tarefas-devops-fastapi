# CRUD de Tarefas — FastAPI

API REST para gerenciamento de tarefas, permitindo criar, listar, consultar, concluir e excluir registros. A aplicação utiliza PostgreSQL para persistência dos dados e conta com um pipeline automatizado de integração e entrega contínua (CI/CD).

## Execução local

1. Clone o repositório:

   ```bash
   git clone https://github.com/mariabergamin18/crud-tarefas-devops-fastapi.git
   cd crud-tarefas-devops-fastapi
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute a aplicação:

   ```bash
   fastapi dev app/api.py
   ```

A documentação interativa estará disponível em: http://127.0.0.1:8000/docs

> **Observação:** Para execução local, é necessário configurar as variáveis de ambiente de conexão com o PostgreSQL. No Render, essas variáveis já estão configuradas na plataforma.

## Endpoints principais

A API disponibiliza as seguintes operações:

| Método | Endpoint | Descrição |
|---|---|---|
| `GET` | `/tarefas` | Lista todas as tarefas. |
| `POST` | `/tarefas` | Cadastra uma nova tarefa. |
| `GET` | `/tarefas/{id_tarefa}` | Consulta uma tarefa pelo ID. |
| `PUT` | `/tarefas/{id_tarefa}` | Marca uma tarefa como concluída. |
| `DELETE` | `/tarefas/{id_tarefa}` | Exclui uma tarefa. |

### Exemplos de requisições

**1. Listar tarefas**

```bash
curl http://localhost:8000/tarefas
```

**2. Criar uma tarefa**

```bash
curl -X POST http://localhost:8000/tarefas \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Estudar DevOps",
    "descricao": "Revisar o pipeline CI/CD"
  }'
```

**3. Consultar uma tarefa**

```bash
curl http://localhost:8000/tarefas/1
```

**4. Concluir uma tarefa**

```bash
curl -X PUT http://localhost:8000/tarefas/1
```

**5. Excluir uma tarefa**

```bash
curl -X DELETE http://localhost:8000/tarefas/1
```

> Substitua `1` pelo ID da tarefa desejada. Os exemplos consideram a aplicação em execução local na porta 8000.

## Tecnologias utilizadas

- **Python 3.14** e **FastAPI** — desenvolvimento da API REST.
- **SQLModel** e **SQLAlchemy** — mapeamento e gerenciamento dos dados.
- **PostgreSQL** e **Psycopg** — banco de dados e conexão.
- **Docker** e **Docker Hub** — containerização e publicação da imagem.
- **GitHub Actions** — automação do pipeline CI/CD, com testes via Pytest e análise de código via Pylint.
- **Render** — hospedagem da aplicação.
