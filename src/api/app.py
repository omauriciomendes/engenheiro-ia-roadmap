from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI(title="Recomendador de Setlists", version="0.1.0")

class ContextoEvento(BaseModel):
    tipo_evento: str
    publico: str
    energia_desejada: str
    clima: str | None = None
    historico_musicas: List[str] | None = None

class Recomendacao(BaseModel):
    proxima_musica: str
    justificativa: str
    features: Dict[str, Any]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/recomendar", response_model=Recomendacao)
def recomendar(ctx: ContextoEvento):
    # Placeholder simples. Substituir por pipeline treinado.
    musica = "Piseiro Clássico"
    justificativa = "Combina com evento e energia desejada segundo regras simples"
    features = {
        "bpm": 128,
        "tonalidade": "A menor",
        "energia": "alta",
        "tipo_evento": ctx.tipo_evento
    }
    return Recomendacao(proxima_musica=musica, justificativa=justificativa, features=features)