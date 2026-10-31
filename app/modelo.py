"""" Modelos """

from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field

class Tarefa(SQLModel, table=True):
    id: int | None = Field(alias="_id", primary_key=True, unique=True, default=None)
    titulo: str
    descricao: Optional[str] = None
    concluida: bool = False
    data_criacao: datetime
    data_conclusao: Optional[datetime] = None

    def finalizar(self):
        """ finalizar tarefa """
        self.concluida = True
        self.data_conclusao = datetime.now().astimezone(timezone.utc)
