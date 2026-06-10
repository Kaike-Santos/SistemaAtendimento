# data/persistencia.py
# Persistência de dados em arquivos JSON.

import json
import os
from typing import Any


DATA_DIR = os.path.join(os.path.dirname(__file__))


def _caminho(nome_arquivo: str) -> str:
    return os.path.join(DATA_DIR, nome_arquivo)


def salvar(nome_arquivo: str, dados: Any) -> None:
    """Salva dados em JSON. Cria o arquivo se não existir."""
    caminho = _caminho(nome_arquivo)
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)


def carregar(nome_arquivo: str, padrao: Any = None) -> Any:
    """Carrega dados de JSON. Retorna `padrao` se o arquivo não existir."""
    caminho = _caminho(nome_arquivo)
    if not os.path.exists(caminho):
        return padrao if padrao is not None else []
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_clientes(lista: list[dict]) -> None:
    salvar("clientes.json", lista)


def carregar_clientes() -> list[dict]:
    return carregar("clientes.json", [])


def salvar_atendentes(lista: list[dict]) -> None:
    salvar("atendentes.json", lista)


def carregar_atendentes() -> list[dict]:
    return carregar("atendentes.json", [])


def salvar_atendimentos(lista: list[dict]) -> None:
    salvar("atendimentos.json", lista)


def carregar_atendimentos() -> list[dict]:
    return carregar("atendimentos.json", [])