# gui/tela_relatorios.py
# Tela de relatórios: tempo médio, top 5 e alertas.

import tkinter as tk
from tkinter import ttk, messagebox
from reports import relatorios
from reports.filtros import alertas_espera_alta
from business import regras_fila


class TelaRelatorios(tk.Frame):
    """Tela de relatórios gerenciais."""

    def __init__(self, master, app) -> None:
        super().__init__(master, bg="#f8f9fa")
        self.app = app
        self._construir()

    def _construir(self) -> None:
        tk.Label(self, text="Relatórios", font=("Helvetica", 16, "bold"), bg="#f8f9fa").pack(pady=12)

        btn_frame = tk.Frame(self, bg="#f8f9fa")
        btn_frame.pack(pady=6)
        tk.Button(btn_frame, text="Tempo médio geral", command=self._tempo_medio, bg="#2b2d42", fg="white", padx=8).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Top 5 clientes", command=self._top5, bg="#2b2d42", fg="white", padx=8).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Tempo médio por atendente", command=self._por_atendente, bg="#2b2d42", fg="white", padx=8).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Alertas de espera", command=self._alertas, bg="#ef233c", fg="white", padx=8).pack(side=tk.LEFT, padx=4)

        self._texto = tk.Text(self, height=20, font=("Courier", 11), bg="#ffffff", relief=tk.FLAT)
        self._texto.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)

    def _escrever(self, conteudo: str) -> None:
        self._texto.config(state=tk.NORMAL)
        self._texto.delete("1.0", tk.END)
        self._texto.insert(tk.END, conteudo)
        self._texto.config(state=tk.DISABLED)

    def _tempo_medio(self) -> None:
        media = relatorios.tempo_medio_atendimento()
        mins, segs = divmod(int(media), 60)
        self._escrever(f"Tempo médio geral de atendimento: {mins}min {segs}s")

    def _top5(self) -> None:
        top = relatorios.top5_clientes()
        if not top:
            self._escrever("Nenhum atendimento registrado.")
            return
        linhas = ["Top 5 clientes mais atendidos:\n"]
        for i, (id_c, qtd) in enumerate(top, start=1):
            linhas.append(f"  {i}. Cliente {id_c}: {qtd} atendimento(s)")
        self._escrever("\n".join(linhas))

    def _por_atendente(self) -> None:
        dados = relatorios.tempo_medio_por_atendente()
        if not dados:
            self._escrever("Nenhum dado disponível.")
            return
        linhas = ["Tempo médio por atendente:\n"]
        for id_at, media in dados.items():
            mins, segs = divmod(int(media), 60)
            linhas.append(f"  Atendente {id_at}: {mins}min {segs}s")
        self._escrever("\n".join(linhas))

    def _alertas(self) -> None:
        fila_atual = [
            {"cliente": c, "entrada": __import__("datetime").datetime.now()}
            for c in regras_fila.listar_fila()
        ]
        alertas = alertas_espera_alta(fila_atual)
        if not alertas:
            self._escrever("Nenhum cliente aguardando acima do limite de espera.")
            return
        linhas = ["Clientes com espera alta:\n"]
        for a in alertas:
            mins, segs = divmod(a["espera_segundos"], 60)
            linhas.append(f"  {a['cliente'].nome}: {mins}min {segs}s aguardando")
        self._escrever("\n".join(linhas))
