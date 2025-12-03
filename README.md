# Roadmap Engenheiro de IA — 90 dias

Este repositório acompanha seu plano de transição de carreira para Engenheiro de IA. 
Carga semanal prevista: 20 horas. Perfil: iniciante. Objetivo: transição de músico para tecnologia. Preferências: dados e código. Cursos de apoio: DIO. Universidade: UNINASSAU.

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

Dica
Aproveite sua vivência como músico. Crie features como andamento, tonalidade, energia, proximidade de hits locais. Conte a história do problema e os ganhos práticos em shows.

## Roteiro de entrevistas

Pergunta 1. Fale sobre um projeto de machine learning que você fez
Como responder
Contexto, objetivo, dados, modelo, métricas, deploy, lições. Use o recomendador.

Pergunta 2. Como você escolhe métricas para um modelo
Como responder
Amarre à tarefa. Classificação pode usar F1 em desbalanceamento, regressão pode usar MAE, recomendação pode usar MAP e cobertura. Traga métrica de negócio.

Pergunta 3. O que é overfitting e como evitar
Como responder
Definição simples, sintomas, validação cruzada, regularização, early stopping, mais dados, simplificar o modelo e monitorar em produção.

Pergunta 4. Como colocar um modelo em produção
Como responder
Empacotar pipeline, criar API, versionar modelo e dados, observabilidade, rollback, testes, segurança e automação com CI.

Pergunta 5. Conte uma situação em que você convenceu alguém com dados
Como responder
Situação, tarefa, ação, resultado. Use exemplo de marketing ou música.

## Trilha DIO recomendada

Trilha: Machine Learning Specialist da DIO. Alternativa complementar. Bootcamp CAIXA Inteligência Artificial na Prática.

Por que
Cobre Python, Pandas, Scikit-learn e bibliotecas modernas com projetos. Conecta fundamentos a prática necessária para Engenheiro de IA. Ajuda a construir portfólio e networking.

Próximos passos
1. Acesse dio.me
2. Busque pela trilha sugerida
3. Inscreva-se
4. Siga o cronograma junto com este roadmap

## Como usar este repositório

* Crie um ambiente. Veja Makefile
* Rode os testes. pytest
* Rastreie experimentos. MLflow
* Suba a API local. FastAPI com uvicorn
* Construa a imagem. Docker

## Estrutura

```
engenheiro-ia-roadmap
├── configs
├── data
├── notebooks
├── reports
└── src
```