# reports/exportar.py
# Exportação de relatórios em CSV.

import csv
import os
from datetime import datetime
from data import persistencia


def exportar_atendimentos(caminho: str | None = None) -> str:
    """
    Exporta o histórico de atendimentos em CSV.
    Retorna o caminho do arquivo gerado.
    """
    if not caminho:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        caminho = os.path.join("data", f"atendimentos_{ts}.csv")

    historico = persistencia.carregar_atendimentos()
    if not historico:
        raise ValueError("Nenhum atendimento registrado para exportar.")

    campos = ["id_atendimento", "id_cliente", "id_atendente", "data_hora", "duracao_segundos"]

    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for a in historico:
            writer.writerow({k: a.get(k, "") for k in campos})

    return caminho


def exportar_clientes(caminho: str | None = None) -> str:
    """Exporta cadastro de clientes em CSV."""
    if not caminho:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        caminho = os.path.join("data", f"clientes_{ts}.csv")

    clientes = persistencia.carregar_clientes()
    if not clientes:
        raise ValueError("Nenhum cliente cadastrado para exportar.")

    campos = ["id_cliente", "nome", "telefone", "prioridade"]

    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for c in clientes:
            writer.writerow({k: c.get(k, "") for k in campos})

    return caminho