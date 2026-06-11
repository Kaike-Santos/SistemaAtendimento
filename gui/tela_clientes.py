# gui/tela_clientes.py
# Tela de cadastro e listagem de clientes.

import tkinter as tk
from tkinter import ttk, messagebox
from business import regras_cliente


class TelaClientes(tk.Frame):
    """Tela de cadastro, busca e listagem de clientes."""

    def __init__(self, master, app) -> None:
        super().__init__(master, bg="#f8f9fa")
        self.app = app
        self._construir()
        self._atualizar_lista()

    def _construir(self) -> None:
        tk.Label(self, text="Clientes", font=("Helvetica", 16, "bold"), bg="#f8f9fa").pack(pady=12)

        form = tk.Frame(self, bg="#f8f9fa")
        form.pack(pady=4)

        campos = [("ID", "id"), ("Nome", "nome"), ("Telefone", "tel")]
        self._vars: dict = {}
        for i, (label, chave) in enumerate(campos):
            tk.Label(form, text=label, bg="#f8f9fa").grid(row=i, column=0, sticky="e", padx=6, pady=3)
            var = tk.StringVar()
            self._vars[chave] = var
            tk.Entry(form, textvariable=var, width=30).grid(row=i, column=1, pady=3)

        self._var_prio = tk.BooleanVar()
        tk.Checkbutton(form, text="Prioritário", variable=self._var_prio, bg="#f8f9fa").grid(
            row=3, column=1, sticky="w"
        )

        btn_frame = tk.Frame(self, bg="#f8f9fa")
        btn_frame.pack(pady=6)
        tk.Button(btn_frame, text="Cadastrar", command=self._cadastrar, bg="#2b2d42", fg="white", padx=10).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Remover selecionado", command=self._remover, bg="#ef233c", fg="white", padx=10).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Atualizar lista", command=self._atualizar_lista, padx=10).pack(side=tk.LEFT, padx=4)

        cols = ("ID", "Nome", "Telefone", "Prioritário")
        self._tree = ttk.Treeview(self, columns=cols, show="headings", height=14)
        for c in cols:
            self._tree.heading(c, text=c)
            self._tree.column(c, width=160)
        self._tree.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)

    def _cadastrar(self) -> None:
        try:
            regras_cliente.cadastrar_cliente(
                self._vars["id"].get(),
                self._vars["nome"].get(),
                self._vars["tel"].get(),
                self._var_prio.get(),
            )
            for v in self._vars.values():
                v.set("")
            self._var_prio.set(False)
            self._atualizar_lista()
            messagebox.showinfo("Sucesso", "Cliente cadastrado.")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def _remover(self) -> None:
        selecionado = self._tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um cliente.")
            return
        id_cliente = self._tree.item(selecionado[0])["values"][0]
        try:
            regras_cliente.remover_cliente(str(id_cliente))
            self._atualizar_lista()
            messagebox.showinfo("Sucesso", f"Cliente {id_cliente} removido.")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def _atualizar_lista(self) -> None:
        for row in self._tree.get_children():
            self._tree.delete(row)
        for c in regras_cliente.listar_clientes():
            self._tree.insert("", tk.END, values=(c.id_cliente, c.nome, c.telefone, "Sim" if c.prioridade else "Não"))