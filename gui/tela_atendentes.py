# gui/tela_atendentes.py
# Tela de cadastro e listagem de atendentes.

import tkinter as tk
from tkinter import ttk, messagebox
from models.atendente import Atendente
from data import persistencia


def _carregar() -> list[Atendente]:
    return [Atendente.de_dict(d) for d in persistencia.carregar_atendentes()]


def _salvar(lista: list[Atendente]) -> None:
    persistencia.salvar_atendentes([a.para_dict() for a in lista])


class TelaAtendentes(tk.Frame):
    """Tela de cadastro e listagem de atendentes."""

    def __init__(self, master, app) -> None:
        super().__init__(master, bg="#f8f9fa")
        self.app = app
        self._construir()
        self._atualizar_lista()

    def _construir(self) -> None:
        tk.Label(self, text="Atendentes", font=("Helvetica", 16, "bold"), bg="#f8f9fa").pack(pady=12)

        form = tk.Frame(self, bg="#f8f9fa")
        form.pack(pady=4)

        self._var_id = tk.StringVar()
        self._var_nome = tk.StringVar()
        for i, (label, var) in enumerate([("ID", self._var_id), ("Nome", self._var_nome)]):
            tk.Label(form, text=label, bg="#f8f9fa").grid(row=i, column=0, sticky="e", padx=6, pady=3)
            tk.Entry(form, textvariable=var, width=30).grid(row=i, column=1, pady=3)

        btn_frame = tk.Frame(self, bg="#f8f9fa")
        btn_frame.pack(pady=6)
        tk.Button(btn_frame, text="Cadastrar", command=self._cadastrar, bg="#2b2d42", fg="white", padx=10).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Atualizar lista", command=self._atualizar_lista, padx=10).pack(side=tk.LEFT, padx=4)

        cols = ("ID", "Nome", "Status")
        self._tree = ttk.Treeview(self, columns=cols, show="headings", height=14)
        for c in cols:
            self._tree.heading(c, text=c)
            self._tree.column(c, width=200)
        self._tree.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)

    def _cadastrar(self) -> None:
        try:
            id_ = Atendente.validar_id(self._var_id.get())
            nome = Atendente.validar_nome(self._var_nome.get())
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
            return
        lista = _carregar()
        if any(a.id_atendente == id_ for a in lista):
            messagebox.showerror("Erro", f"Atendente '{id_}' já existe.")
            return
        lista.append(Atendente(id_, nome))
        _salvar(lista)
        self._var_id.set("")
        self._var_nome.set("")
        self._atualizar_lista()
        messagebox.showinfo("Sucesso", "Atendente cadastrado.")

    def _atualizar_lista(self) -> None:
        for row in self._tree.get_children():
            self._tree.delete(row)
        for a in _carregar():
            status = "Ocupado" if a.ocupado else "Livre"
            self._tree.insert("", tk.END, values=(a.id_atendente, a.nome, status))