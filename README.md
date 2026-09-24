![CI](https://github.com/omauriciomendes/engenheiro-ia-roadmap/actions/workflows/ci.yml/badge.svg)

# Roadmap Engenheiro de IA: 90 dias

Este repositório acompanha o meu plano de transição de carreira, de músico para Engenheiro de IA, e o projeto prático que nasce dele.

* Carga semanal prevista: 20 horas
* Ponto de partida: iniciante
* Preferências: dados e código
* Apoio: cursos da DIO e graduação na UNINASSAU

## Visão do dia a dia

Como é o trabalho de um Engenheiro de IA:
* Traduzir problemas de negócio em soluções com modelos de machine learning
* Preparar dados, criar features, treinar e avaliar modelos
* Versionar experimentos, ajustar hiperparâmetros e monitorar métricas
* Empacotar e publicar modelos em APIs ou pipelines
* Colaborar com produto, dados e engenharia para levar IA para produção

## Mapa de skills

Core skills:
* Programação com Python, Git, testes
* Estatística básica e aprendizado de máquina supervisionado e não supervisionado
* Manipulação de dados com Pandas, SQL e visualização

Nice to have:
* Deploy com FastAPI, Docker e CI
* MLOps com MLflow ou DVC e monitoramento

Ferramentas e tecnologias:
* Python, Jupyter, Pandas, NumPy, Scikit-learn
* SQL, PostgreSQL
* FastAPI, Docker, MLflow, GitHub

## Roadmap de 90 dias

Adaptado para 20 horas por semana

Mês 1 fundamentos
* Semanas 1 a 2
  * Python para dados. Estruturas, funções, POO leve, virtualenv, testes
  * Git e GitHub. Fluxo de branch, pull requests, issues
* Semanas 3 a 4
  * Estatística prática. Média, variância, distribuições, correlação, amostragem
  * Pandas e SQL. Limpeza, joins, groupby, janelas, consultas essenciais

Mês 2 prática
* Semanas 5 a 6
  * Machine learning com Scikit-learn. Pipeline, validação cruzada, métricas por tarefa
  * Modelos clássicos. Regressão, árvores, ensembles, SVM, K-means
* Semanas 7 a 8
  * Engenharia de features. Normalização, encoding, leakage, seleção
  * Experimentos reprodutíveis. MLflow ou DVC, tracking de métricas

Mês 3 portfólio e preparação
* Semanas 9 a 10
  * API de inferência com FastAPI. Dockerização. Documentação OpenAPI
  * Banco de dados e logs. Persistir previsões e latência
* Semanas 11 a 12
  * Monitoramento de modelo. Drift e métricas em produção
  * Entrevistas, currículo e LinkedIn. Projeto final publicado e README caprichado

## Projeto de portfólio

Projeto: Recomendador de Setlists Inteligente para Bandas e Eventos

O que fazer
* Coletar ou organizar dados de setlists, gêneros, bpm, tonalidade e reações do público
* Treinar modelo de recomendação para próxima música com variações de contexto
* Expor API que recebe o contexto do evento e retorna recomendações

Entregáveis
* Repositório com EDA em notebook e pipeline de treino em src/pipeline
* API FastAPI em src/api com endpoint de recomendação e documentação
* Dashboard simples de métricas de modelo e monitoramento de drift

Critérios de aceitação
* Reprodutibilidade do treino com seed e requirements
* Métricas claras. Top-K accuracy ou MAP e latência da API
* README com arquitetura, decisões de design e exemplos de uso

### Onde o projeto está hoje

| Parte | Estado |
| --- | --- |
| API FastAPI com `/health` e `/recomendar` | Pronta, com testes. Por enquanto devolve sempre a mesma música, sem modelo treinado |
| Pipeline de treino (scikit-learn, MLflow, métrica Top-3) | Escrito, esperando dados |
| Dataset `data/processed/setlists.csv` | Só o cabeçalho. Próximo passo: organizar os setlists dos meus shows |
| Checagem de drift | Função que alerta quando uma métrica varia mais de 20% |
| CI no GitHub Actions (pre-commit, ruff, pytest) | Configurado |

## Como usar este repositório

* Crie um ambiente. Veja Makefile
* Rode os testes. pytest
* Rastreie experimentos. MLflow
* Suba a API local. FastAPI com uvicorn
* Construa a imagem. Docker

## Estrutura

```
engenheiro-ia-roadmap
├── data/processed      dados de setlists (CSV)
├── src/api             API de recomendação (FastAPI)
├── src/pipeline        treino do modelo (scikit-learn + MLflow)
├── src/monitoring      checagem de drift
├── tests               testes da API
├── ROADMAP_90_DIAS.md  metas semana a semana
└── Makefile            setup, testes, lint e API
```
