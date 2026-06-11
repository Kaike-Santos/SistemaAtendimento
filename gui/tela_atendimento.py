# gui/tela_atendimento.py
# Tela para chamar próximo cliente e finalizar atendimento.

import tkinter as tk
from tkinter import ttk, messagebox
from business import regras_atendimento
from models.atendente import Atendente
from data import persistencia


class TelaAtendimento(tk.Frame):
    """Tela de abertura e finalização de atendimentos."""

    def __init__(self, master, app) -> None:
        super().__init__(master, bg="#f8f9fa")
        self.app = app
        self._construir()

    def _construir(self) -> None:
        tk.Label(self, text="Atendimento", font=("Helvetica", 16, "bold"), bg="#f8f9fa").pack(pady=12)

        form = tk.Frame(self, bg="#f8f9fa")
        form.pack(pady=4)
        tk.Label(form, text="ID do Atendente:", bg="#f8f9fa").grid(row=0, column=0, padx=6, pady=4)
        self._var_atendente = tk.StringVar()
        tk.Entry(form, textvariable=self._var_atendente, width=20).grid(row=0, column=1)

        btn_frame = tk.Frame(self, bg="#f8f9fa")
        btn_frame.pack(pady=8)
        tk.Button(btn_frame, text="Chamar próximo", command=self._abrir, bg="#2b2d42", fg="white", padx=10).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Finalizar atendimento", command=self._finalizar, bg="#ef233c", fg="white", padx=10).pack(side=tk.LEFT, padx=4)

        self._label_info = tk.Label(self, text="", bg="#f8f9fa", font=("Helvetica", 12), wraplength=500)
        self._label_info.pack(pady=12)

        tk.Label(self, text="Atendimentos em aberto:", bg="#f8f9fa", font=("Helvetica", 12, "bold")).pack()
        cols = ("Atendente", "Cliente")
        self._tree = ttk.Treeview(self, columns=cols, show="headings", height=8)
        for c in cols:
            self._tree.heading(c, text=c)
            self._tree.column(c, width=200)
        self._tree.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)
        self._atualizar_tree()

    def _abrir(self) -> None:
        id_at = self._var_atendente.get().strip()
        if not id_at:
            messagebox.showwarning("Aviso", "Informe o ID do atendente.")
            return
        try:
            cliente = regras_atendimento.abrir_atendimento(id_at)
            self._label_info.config(text=f"Atendendo: {cliente.nome} ({cliente.id_cliente})")
            self._atualizar_tree()
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def _finalizar(self) -> None:
        id_at = self._var_atendente.get().strip()
        if not id_at:
            messagebox.showwarning("Aviso", "Informe o ID do atendente.")
            return
        try:
            registro = regras_atendimento.finalizar_atendimento(id_at)
            mins, segs = divmod(registro.duracao_segundos, 60)
            self._label_info.config(text=f"Finalizado! Duração: {mins}min {segs}s")
            self._atualizar_tree()
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def _atualizar_tree(self) -> None:
        for row in self._tree.get_children():
            self._tree.delete(row)
        for id_at, (cliente, _) in regras_atendimento.atendimentos_em_aberto().items():
            self._tree.insert("", tk.END, values=(id_at, cliente.id_cliente))
