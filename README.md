# ish-challenge
Autor: Larissa Morais

## Motivação

Esse é um software desenvolvido para o desafio da empresa ish. O programa foi desenvolvido utilizando a linguagem python 3.9 juntamente com o framework FastAPI. O framework foi escolhido pois foram possibilita maior performace além da programação async. Além disso, foram utilizadas bibliotecas como requests para chamadas externas.

## Requisitos

- docker (versão recomendada: 20.10)
- docker compose (versão recomendada: 1.29)

## Instalação


```bash
docker-compose up --build
```

## API Prescription
#### Pegar uma playlist

```http
  GET /get_music_recommendations
```

| Parâmetro   | Tipo       |
| :---------- | :--------- |
| `lat` | `int` |
| `lon` | `str` |
| `city` | `str` |

```http
  ex: http://0.0.0.0:8000/get_music_recommendations/?city=florianopolis
```
```http
  ex: http://0.0.0.0:8000/get_music_recommendations/?lat=-27.670094797245927&lon=-48.73918829600568
```
#### Pegar uma playlist

```http
  GET /get_music_recommendations
```

| Parâmetro   | Tipo       |
| :---------- | :--------- |
| `lat` | `int` |
| `lon` | `str` |
| `city` | `str` |

## Pendências e melhorias
- Criação de Testes com pytest
- Utilizar cache(REDIS) e banco de dados como backup para a API
