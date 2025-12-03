from fastapi.testclient import TestClient
from src.api.app import app

def test_recomendar():
    c = TestClient(app)
    payload = {
        "tipo_evento": "barzinho",
        "publico": "adulto",
        "energia_desejada": "média",
        "clima": "festa",
        "historico_musicas": ["Exemplo A", "Exemplo B"]
    }
    r = c.post("/recomendar", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert "proxima_musica" in body
    assert "justificativa" in body
    assert "features" in body
