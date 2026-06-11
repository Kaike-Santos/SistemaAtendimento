# reports/ordenacao.py
# Algoritmos de ordenação para relatórios.
# Merge sort: O(n log n) — usado para ordenar por duração.
# Quick sort: O(n log n) médio — usado para top 5 clientes.


def merge_sort(lista: list, chave) -> list:
    """
    Merge sort estável — O(n log n).
    Ordena a lista pelo valor retornado por `chave(item)`.
    """
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esq = merge_sort(lista[:meio], chave)
    dir_ = merge_sort(lista[meio:], chave)
    return _merge(esq, dir_, chave)


def _merge(esq: list, dir_: list, chave) -> list:
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir_):
        if chave(esq[i]) <= chave(dir_[j]):
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir_[j])
            j += 1
    resultado.extend(esq[i:])
    resultado.extend(dir_[j:])
    return resultado


def quick_sort(lista: list, chave) -> list:
    """
    Quick sort — O(n log n) médio, O(n²) pior caso.
    Ordena em ordem decrescente pelo valor de `chave(item)`.
    """
    if len(lista) <= 1:
        return lista
    pivo = chave(lista[len(lista) // 2])
    menores = [x for x in lista if chave(x) > pivo]   # decrescente
    iguais = [x for x in lista if chave(x) == pivo]
    maiores = [x for x in lista if chave(x) < pivo]
    return quick_sort(menores, chave) + iguais + quick_sort(maiores, chave)