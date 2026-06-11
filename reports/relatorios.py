# reports/relatorios.py
# Geração de relatórios: tempo médio e top 5 clientes.

from reports.ordenacao import merge_sort, quick_sort
from reports.recursao import contar_atendimentos_por_cliente
from data import persistencia


def tempo_medio_atendimento() -> float:
    """
    Calcula o tempo médio de todos os atendimentos finalizados.
    Retorna duração média em segundos.
    """
    historico = persistencia.carregar_atendimentos()
    if not historico:
        return 0.0
    total = sum(a.get("duracao_segundos", 0) for a in historico)
    return total / len(historico)


def tempo_medio_por_atendente() -> dict:
    """Retorna dict {id_atendente: media_segundos}."""
    historico = persistencia.carregar_atendimentos()
    agrupado: dict = {}
    for a in historico:
        id_at = a.get("id_atendente", "")
        if id_at not in agrupado:
            agrupado[id_at] = []
        agrupado[id_at].append(a.get("duracao_segundos", 0))
    return {k: sum(v) / len(v) for k, v in agrupado.items()}


def top5_clientes() -> list:
    """
    Retorna os 5 clientes mais atendidos usando quick sort decrescente.
    Retorna lista de (id_cliente, quantidade).
    """
    historico = persistencia.carregar_atendimentos()
    contagem = contar_atendimentos_por_cliente(historico)
    pares = list(contagem.items())
    ordenado = quick_sort(pares, chave=lambda x: x[1])
    return ordenado[:5]


def relatorio_ordenado_por_duracao() -> list:
    """Retorna histórico completo ordenado por duração crescente via merge sort."""
    historico = persistencia.carregar_atendimentos()
    return merge_sort(historico, chave=lambda a: a.get("duracao_segundos", 0))