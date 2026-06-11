# business/regras_cliente.py
# Regras de cadastro e remoção de clientes.

from models.cliente import Cliente
from structures.lista_encadeada import ListaEncadeada
from structures.vetor_ordenado import VetorOrdenado
from business.regras_atendimento import atendimentos_em_aberto
from data import persistencia

import logging

logger = logging.getLogger(__name__)

_lista_ativos = ListaEncadeada()
_vetor_busca = VetorOrdenado()


def _carregar_clientes() -> None:
    dados = persistencia.carregar_clientes()

    for d in dados:
        cliente = Cliente.de_dict(d)

        _lista_ativos.inserir(cliente)
        _vetor_busca.inserir(cliente)


def cadastrar_cliente(
    id_cliente: str,
    nome: str,
    telefone: str,
    prioridade: bool = False,
) -> Cliente:

    id_cliente = Cliente.validar_id(id_cliente)
    nome = Cliente.validar_nome(nome)
    telefone = Cliente.validar_telefone(telefone)

    if _vetor_busca.buscar(id_cliente):
        raise ValueError(
            f"Cliente com id '{id_cliente}' já existe."
        )

    cliente = Cliente(
        id_cliente,
        nome,
        telefone,
        prioridade,
    )

    _lista_ativos.inserir(cliente)
    _vetor_busca.inserir(cliente)

    _salvar()

    logger.info("Cliente cadastrado: %s", cliente)

    return cliente


def remover_cliente(id_cliente: str) -> bool:
    em_aberto = atendimentos_em_aberto()

    for atendente_id, (cliente, _) in em_aberto.items():
        if cliente.id_cliente == id_cliente:
            raise ValueError(
                f"Cliente {id_cliente} possui atendimento "
                f"em aberto com atendente {atendente_id}."
            )

    removido_lista = _lista_ativos.remover(id_cliente)
    removido_vetor = _vetor_busca.remover(id_cliente)

    if removido_lista or removido_vetor:
        _salvar()

        logger.info(
            "Cliente removido: %s",
            id_cliente,
        )

        return True

    return False


def buscar_cliente(id_cliente: str):
    return _vetor_busca.buscar(id_cliente)


def listar_clientes() -> list:
    return _lista_ativos.listar()


def _salvar() -> None:
    dados = [
        cliente.para_dict()
        for cliente in _lista_ativos.listar()
    ]

    persistencia.salvar_clientes(dados)


_carregar_clientes()