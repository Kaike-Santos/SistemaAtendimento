# reports/recursao.py
# Busca recursiva no histórico de atendimentos por id de cliente.
# Complexidade: O(n) — percorre a lista recursivamente.


def buscar_historico_cliente(historico: list, id_cliente: str, indice: int = 0) -> list:
    """
    Busca recursiva todos os atendimentos de um cliente.
    historico: lista de dicts com campo 'id_cliente'.
    Retorna lista de atendimentos que pertencem ao cliente.
    Complexidade: O(n).
    """
    if indice >= len(historico):
        return []
    atual = historico[indice]
    resto = buscar_historico_cliente(historico, id_cliente, indice + 1)
    if atual.get("id_cliente") == id_cliente:
        return [atual] + resto
    return resto


def contar_atendimentos_por_cliente(historico: list, contagem: dict | None = None, indice: int = 0) -> dict:
    """
    Conta recursivamente quantos atendimentos cada cliente teve.
    Retorna dict {id_cliente: quantidade}.
    Complexidade: O(n).
    """
    if contagem is None:
        contagem = {}
    if indice >= len(historico):
        return contagem
    id_c = historico[indice].get("id_cliente", "")
    contagem[id_c] = contagem.get(id_c, 0) + 1
    return contar_atendimentos_por_cliente(historico, contagem, indice + 1)