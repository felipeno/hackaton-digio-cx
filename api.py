from typing import List, Dict

from fastapi import FastAPI
from pydantic import BaseModel


class Incidente(BaseModel):
    nome: str
    codigo: str
    gatilhos: List[Dict]
    grupoUsuarios: str
    comunicacaoExterna: Dict
    comunicacaoInterna: List[Dict]


app = FastAPI()


@app.post("/339")
def entrada(incidente: Incidente):
    return {"message": "Hello World"}
