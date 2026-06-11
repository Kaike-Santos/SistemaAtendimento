# gui/janela_principal.py
# Janela principal com menu lateral e navegação entre telas.

import tkinter as tk
from tkinter import ttk


class JanelaPrincipal(tk.Tk):
    """Janela raiz com menu lateral e área de conteúdo."""

    MENU_ITENS = [
        ("Clientes", "tela_clientes"),
        ("Atendentes", "tela_atendentes"),
        ("Fila", "tela_fila"),
        ("Atendimento", "tela_atendimento"),
        ("Histórico", "tela_historico"),
        ("Relatórios", "tela_relatorios"),
        ("Desfazer", "tela_desfazer"),
        ("Exportar", "tela_exportar"),
    ]

    def __init__(self) -> None:
        super().__init__()
        self.title("Sistema de Atendimento")
        self.geometry("900x600")
        self.resizable(True, True)
        self._frames: dict = {}
        self._construir_layout()
        self.mostrar_tela("tela_clientes")

    def _construir_layout(self) -> None:
        # Menu lateral
        menu = tk.Frame(self, width=180, bg="#2b2d42")
        menu.pack(side=tk.LEFT, fill=tk.Y)
        menu.pack_propagate(False)

        titulo = tk.Label(
            menu, text="Atendimento\nSistema",
            bg="#2b2d42", fg="#edf2f4",
            font=("Helvetica", 13, "bold"),
            pady=20,
        )
        titulo.pack()

        for rotulo, chave in self.MENU_ITENS:
            btn = tk.Button(
                menu, text=rotulo,
                bg="#2b2d42", fg="#edf2f4",
                activebackground="#8d99ae",
                font=("Helvetica", 11),
                relief=tk.FLAT, cursor="hand2",
                command=lambda c=chave: self.mostrar_tela(c),
                padx=10, pady=8, anchor="w",
            )
            btn.pack(fill=tk.X, padx=8, pady=2)

        # Área de conteúdo
        self._area = tk.Frame(self, bg="#f8f9fa")
        self._area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def registrar_tela(self, chave: str, frame: tk.Frame) -> None:
        self._frames[chave] = frame

    def mostrar_tela(self, chave: str) -> None:
        for f in self._frames.values():
            f.pack_forget()
        tela = self._frames.get(chave)
        if tela:
            tela.pack(fill=tk.BOTH, expand=True)
        else:
            self._carregar_tela(chave)

    def _carregar_tela(self, chave: str) -> None:
        """Importação lazy para não circular no início."""
        modulo_map = {
            "tela_clientes": ("gui.tela_clientes", "TelaClientes"),
            "tela_atendentes": ("gui.tela_atendentes", "TelaAtendentes"),
            "tela_fila": ("gui.tela_fila", "TelaFila"),
            "tela_atendimento": ("gui.tela_atendimento", "TelaAtendimento"),
            "tela_historico": ("gui.tela_historico", "TelaHistorico"),
            "tela_relatorios": ("gui.tela_relatorios", "TelaRelatorios"),
            "tela_desfazer": ("gui.tela_desfazer", "TelaDesfazer"),
            "tela_exportar": ("gui.tela_exportar", "TelaExportar"),
        }
        if chave not in modulo_map:
            return
        nome_modulo, nome_classe = modulo_map[chave]
        import importlib
        modulo = importlib.import_module(nome_modulo)
        Classe = getattr(modulo, nome_classe)
        frame = Classe(self._area, self)
        self._frames[chave] = frame
        frame.pack(fill=tk.BOTH, expand=True)