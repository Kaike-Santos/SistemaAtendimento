# business/regras_atendimento.py

import uuid
from datetime import datetime

from models.atendimento import Atendimento
from structures.pilha import Pilha
from business.regras_fila import chamar_proximo, fila_vazia
from data import persistencia

import logging

logger = logging.getLogger(__name__)

_pilha_desfazer: Pilha = Pilha()
_atendimentos_em_aberto: dict = {}


def abrir_atendimento(id_atendente: str):
    if fila_vazia():
        raise ValueError("Fila vazia. Nenhum cliente aguardando.")

    if id_atendente in _atendimentos_em_aberto:
        raise ValueError(
            f"Atendente {id_atendente} já está em atendimento."
        )

    cliente = chamar_proximo()

    _atendimentos_em_aberto[id_atendente] = (
        cliente,
        datetime.now()
    )

    logger.info(
        "Atendimento aberto: atendente=%s cliente=%s",
        id_atendente,
        cliente.id_cliente,
    )

    return cliente


def finalizar_atendimento(id_atendente: str) -> Atendimento:
    if id_atendente not in _atendimentos_em_aberto:
        raise ValueError(
            f"Atendente {id_atendente} não possui atendimento em aberto."
        )

    cliente, inicio = _atendimentos_em_aberto.pop(id_atendente)

    duracao = int(
        (datetime.now() - inicio).total_seconds()
    )

    registro = Atendimento(
        id_atendimento=str(uuid.uuid4())[:8],
        id_cliente=cliente.id_cliente,
        id_atendente=id_atendente,
        data_hora=datetime.now(),
        duracao_segundos=duracao,
    )

    historico = persistencia.carregar_atendimentos()
    historico.append(registro.para_dict())

    persistencia.salvar_atendimentos(historico)

    _pilha_desfazer.push(registro)

    logger.info(
        "Atendimento finalizado: %s",
        registro,
    )

    return registro


def desfazer_ultima_finalizacao():
    ultimo = _pilha_desfazer.pop()

    if not ultimo:
        return None

    historico = persistencia.carregar_atendimentos()

    historico = [
        a
        for a in historico
        if a["id_atendimento"] != ultimo.id_atendimento
    ]

    persistencia.salvar_atendimentos(historico)

    logger.info(
        "Desfez finalizacao: %s",
        ultimo.id_atendimento,
    )

    return ultimo


def atendimentos_em_aberto() -> dict:
    return dict(_atendimentos_em_aberto)