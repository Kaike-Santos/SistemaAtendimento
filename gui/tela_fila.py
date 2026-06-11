# gui/tela_fila.py
# Tela de visualização da fila e entrada de clientes.

import tkinter as tk
from tkinter import ttk, messagebox
from business import regras_fila, regras_cliente


class TelaFila(tk.Frame):
    """Visualização da fila atual e adição de cliente à fila."""

    def __init__(self, master, app) -> None:
        super().__init__(master, bg="#f8f9fa")
        self.app = app
        self._construir()
        self._atualizar_lista()

    def _construir(self) -> None:
        tk.Label(self, text="Fila de Atendimento", font=("Helvetica", 16, "bold"), bg="#f8f9fa").pack(pady=12)

        form = tk.Frame(self, bg="#f8f9fa")
        form.pack(pady=4)
        tk.Label(form, text="ID do Cliente:", bg="#f8f9fa").grid(row=0, column=0, padx=6)
        self._var_id = tk.StringVar()
        tk.Entry(form, textvariable=self._var_id, width=20).grid(row=0, column=1)

        btn_frame = tk.Frame(self, bg="#f8f9fa")
        btn_frame.pack(pady=6)
        tk.Button(btn_frame, text="Entrar na fila", command=self._entrar, bg="#2b2d42", fg="white", padx=10).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Atualizar", command=self._atualizar_lista, padx=10).pack(side=tk.LEFT, padx=4)

        self._label_total = tk.Label(self, text="Na fila: 0", bg="#f8f9fa", font=("Helvetica", 11))
        self._label_total.pack()

        cols = ("Posição", "ID", "Nome", "Prioridade")
        self._tree = ttk.Treeview(self, columns=cols, show="headings", height=14)
        for c in cols:
            self._tree.heading(c, text=c)
            self._tree.column(c, width=160)
        self._tree.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)

    def _entrar(self) -> None:
        id_cliente = self._var_id.get().strip()
        if not id_cliente:
            messagebox.showwarning("Aviso", "Informe o ID do cliente.")
            return
        cliente = regras_cliente.buscar_cliente(id_cliente)
        if not cliente:
            messagebox.showerror("Erro", f"Cliente '{id_cliente}' não encontrado.")
            return
        regras_fila.entrar_na_fila(cliente)
        self._var_id.set("")
        self._atualizar_lista()
        messagebox.showinfo("Sucesso", f"{cliente.nome} entrou na fila.")

    def _atualizar_lista(self) -> None:
        for row in self._tree.get_children():
            self._tree.delete(row)
        for i, c in enumerate(regras_fila.listar_fila(), start=1):
            prio = "Sim" if c.prioridade else "Não"
            self._tree.insert("", tk.END, values=(i, c.id_cliente, c.nome, prio))
        self._label_total.config(text=f"Na fila: {regras_fila.tamanho_fila()}")
