# reports/filtros.py
# Filtros por data e alertas de tempo de espera alto.

from datetime import datetime
from data import persistencia

LIMITE_ESPERA_SEGUNDOS = 600  # 10 minutos


def filtrar_por_data(data_inicio: datetime, data_fim: datetime) -> list:
    """
    Retorna atendimentos finalizados entre data_inicio e data_fim.
    Complexidade: O(n).
    """
    historico = persistencia.carregar_atendimentos()
    resultado = []
    for a in historico:
        try:
            dt = datetime.fromisoformat(a.get("data_hora", ""))
            if data_inicio <= dt <= data_fim:
                resultado.append(a)
        except ValueError:
            continue
    return resultado


def alertas_espera_alta(fila_atual: list) -> list:
    """
    Recebe a lista atual de clientes em espera com timestamps de entrada.
    Retorna lista de clientes esperando acima do limite definido.
    fila_atual: lista de dicts com {'cliente': Cliente, 'entrada': datetime}.
    """
    agora = datetime.now()
    alertas = []
    for item in fila_atual:
        espera = (agora - item["entrada"]).total_seconds()
        if espera >= LIMITE_ESPERA_SEGUNDOS:
            alertas.append({
                "cliente": item["cliente"],
                "espera_segundos": int(espera),
            })
    return alertas
