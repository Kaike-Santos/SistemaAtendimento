# gui/tela_exportar.py
# Tela de exportação de relatórios em CSV.

import tkinter as tk
from tkinter import messagebox, filedialog
from reports.exportar import exportar_atendimentos, exportar_clientes


class TelaExportar(tk.Frame):
    """Tela de exportação de dados em CSV."""

    def __init__(self, master, app) -> None:
        super().__init__(master, bg="#f8f9fa")
        self.app = app
        self._construir()

    def _construir(self) -> None:
        tk.Label(self, text="Exportar Relatórios", font=("Helvetica", 16, "bold"), bg="#f8f9fa").pack(pady=24)

        tk.Label(
            self,
            text="Exporte os dados do sistema em formato CSV para análise externa.",
            bg="#f8f9fa", font=("Helvetica", 11),
        ).pack(pady=8)

        btn_frame = tk.Frame(self, bg="#f8f9fa")
        btn_frame.pack(pady=16)

        tk.Button(
            btn_frame, text="Exportar atendimentos (CSV)",
            command=self._exportar_atendimentos,
            bg="#2b2d42", fg="white", padx=12, pady=6,
            font=("Helvetica", 11),
        ).pack(pady=6)

        tk.Button(
            btn_frame, text="Exportar clientes (CSV)",
            command=self._exportar_clientes,
            bg="#2b2d42", fg="white", padx=12, pady=6,
            font=("Helvetica", 11),
        ).pack(pady=6)

        self._label_resultado = tk.Label(self, text="", bg="#f8f9fa", font=("Helvetica", 10))
        self._label_resultado.pack(pady=8)

    def _exportar_atendimentos(self) -> None:
        caminho = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV", "*.csv")],
            initialfile="atendimentos.csv",
        )
        if not caminho:
            return
        try:
            exportar_atendimentos(caminho)
            self._label_resultado.config(text=f"Exportado: {caminho}", fg="#2b7a0b")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def _exportar_clientes(self) -> None:
        caminho = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV", "*.csv")],
            initialfile="clientes.csv",
        )
        if not caminho:
            return
        try:
            exportar_clientes(caminho)
            self._label_resultado.config(text=f"Exportado: {caminho}", fg="#2b7a0b")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
