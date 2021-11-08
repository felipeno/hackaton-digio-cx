from typing import List, Dict

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from core import Core


class Gatilhos(BaseModel):
    gatilhos: List[Dict]


app = FastAPI()
core = Core()


@app.post("/339")
async def entrada(gatilhos: Gatilhos):
    if core.valida_incidente(gatilhos):
        core.contabiliza_ocorrencia(gatilhos)
        return core.comunicacao(gatilhos)
    else:
        return core.cria_incidente(gatilhos)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
