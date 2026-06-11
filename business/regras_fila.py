# business/regras_fila.py
# Regras de chamada do próximo atendimento considerando prioridade.

from structures.fila_prioridade import FilaPrioridade


_fila: FilaPrioridade = FilaPrioridade()


def obter_fila() -> FilaPrioridade:
    return _fila


def entrar_na_fila(cliente) -> None:
    _fila.enqueue(cliente)


def chamar_proximo():
    if _fila.vazia():
        return None

    return _fila.dequeue()


def fila_vazia() -> bool:
    return _fila.vazia()


def listar_fila() -> list:
    return _fila.listar()


def tamanho_fila() -> int:
    return len(_fila)