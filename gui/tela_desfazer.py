# gui/tela_desfazer.py
# Tela para desfazer a última finalização de atendimento via pilha.

import tkinter as tk
from tkinter import messagebox
from business import regras_atendimento


class TelaDesfazer(tk.Frame):
    """Tela de desfazer última finalização."""

    def __init__(self, master, app) -> None:
        super().__init__(master, bg="#f8f9fa")
        self.app = app
        self._construir()

    def _construir(self) -> None:
        tk.Label(self, text="Desfazer Última Finalização", font=("Helvetica", 16, "bold"), bg="#f8f9fa").pack(pady=24)

        tk.Label(
            self,
            text=(
                "Esta ação remove o último atendimento finalizado do histórico.\n"
                "A operação usa uma Pilha (LIFO) — O(1).\n"
                "Não é possível desfazer mais de uma vez consecutiva sem novo atendimento."
            ),
            bg="#f8f9fa", font=("Helvetica", 11), wraplength=480, justify="center",
        ).pack(pady=12)

        tk.Button(
            self, text="Desfazer último atendimento",
            command=self._desfazer,
            bg="#ef233c", fg="white",
            font=("Helvetica", 12, "bold"),
            padx=16, pady=8,
        ).pack(pady=16)

        self._label_resultado = tk.Label(self, text="", bg="#f8f9fa", font=("Helvetica", 11))
        self._label_resultado.pack(pady=8)

    def _desfazer(self) -> None:
        resultado = regras_atendimento.desfazer_ultima_finalizacao()
        if resultado:
            self._label_resultado.config(
                text=f"Desfeito: atendimento {resultado.id_atendimento} "
                     f"(cliente {resultado.id_cliente}) removido do histórico.",
                fg="#2b7a0b",
            )
        else:
            self._label_resultado.config(text="Nada para desfazer.", fg="#c0392b")
