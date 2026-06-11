# gui/tela_historico.py
# Histórico de atendimentos por cliente com filtro por data.

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from reports.recursao import buscar_historico_cliente
from data import persistencia


class TelaHistorico(tk.Frame):
    """Tela de histórico de atendimentos com filtro por cliente e data."""

    def __init__(self, master, app) -> None:
        super().__init__(master, bg="#f8f9fa")
        self.app = app
        self._construir()

    def _construir(self) -> None:
        tk.Label(self, text="Histórico de Atendimentos", font=("Helvetica", 16, "bold"), bg="#f8f9fa").pack(pady=12)

        form = tk.Frame(self, bg="#f8f9fa")
        form.pack(pady=4)

        self._var_id = tk.StringVar()
        self._var_inicio = tk.StringVar(value="2020-01-01")
        self._var_fim = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))

        for i, (label, var) in enumerate([
            ("ID do Cliente", self._var_id),
            ("Data início (AAAA-MM-DD)", self._var_inicio),
            ("Data fim (AAAA-MM-DD)", self._var_fim),
        ]):
            tk.Label(form, text=label, bg="#f8f9fa").grid(row=i, column=0, sticky="e", padx=6, pady=3)
            tk.Entry(form, textvariable=var, width=24).grid(row=i, column=1, pady=3)

        btn_frame = tk.Frame(self, bg="#f8f9fa")
        btn_frame.pack(pady=6)
        tk.Button(btn_frame, text="Buscar", command=self._buscar, bg="#2b2d42", fg="white", padx=10).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Ver tudo", command=self._ver_tudo, padx=10).pack(side=tk.LEFT, padx=4)

        cols = ("ID Atend.", "Cliente", "Atendente", "Data/Hora", "Duração (s)")
        self._tree = ttk.Treeview(self, columns=cols, show="headings", height=14)
        for c in cols:
            self._tree.heading(c, text=c)
            self._tree.column(c, width=140)
        self._tree.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)

    def _buscar(self) -> None:
        id_cliente = self._var_id.get().strip()
        try:
            inicio = datetime.strptime(self._var_inicio.get().strip(), "%Y-%m-%d")
            fim = datetime.strptime(self._var_fim.get().strip(), "%Y-%m-%d").replace(hour=23, minute=59)
        except ValueError:
            messagebox.showerror("Erro", "Datas inválidas. Use o formato AAAA-MM-DD.")
            return
        historico = persistencia.carregar_atendimentos()
        if id_cliente:
            historico = buscar_historico_cliente(historico, id_cliente)
        filtrado = [
            a for a in historico
            if inicio <= datetime.fromisoformat(a.get("data_hora", "2000-01-01")) <= fim
        ]
        self._preencher(filtrado)

    def _ver_tudo(self) -> None:
        self._preencher(persistencia.carregar_atendimentos())

    def _preencher(self, lista: list) -> None:
        for row in self._tree.get_children():
            self._tree.delete(row)
        for a in lista:
            self._tree.insert("", tk.END, values=(
                a.get("id_atendimento", ""),
                a.get("id_cliente", ""),
                a.get("id_atendente", ""),
                a.get("data_hora", "")[:16],
                a.get("duracao_segundos", ""),
            ))