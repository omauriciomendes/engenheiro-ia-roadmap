# API de Recomendação

Como rodar local
1. make setup
2. make api
3. Acesse http://localhost:8000/docs

Exemplo de requisição
POST /recomendar
{
  "tipo_evento": "barzinho",
  "publico": "adulto",
  "energia_desejada": "média",
  "clima": "festa",
  "historico_musicas": ["Música A", "Música B"]
}