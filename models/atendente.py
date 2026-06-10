# models/atendente.py
# Classe Atendente com validações.


class Atendente:
    """Representa um atendente cadastrado no sistema."""

    def __init__(self, id_atendente: str, nome: str) -> None:
        self.id_atendente = id_atendente
        self.nome = nome
        self.ocupado = False  # True quando está em atendimento

    # ------------------------------------------------------------------
    # Validações
    # ------------------------------------------------------------------

    @staticmethod
    def validar_id(valor: str) -> str:
        valor = valor.strip()
        if not valor:
            raise ValueError("ID do atendente não pode ser vazio.")
        return valor

    @staticmethod
    def validar_nome(valor: str) -> str:
        valor = valor.strip()
        if not valor:
            raise ValueError("Nome do atendente não pode ser vazio.")
        return valor

    # ------------------------------------------------------------------
    # Serialização
    # ------------------------------------------------------------------

    def para_dict(self) -> dict:
        return {
            "id_atendente": self.id_atendente,
            "nome": self.nome,
            "ocupado": self.ocupado,
        }

    @classmethod
    def de_dict(cls, dados: dict) -> "Atendente":
        obj = cls(
            id_atendente=dados["id_atendente"],
            nome=dados["nome"],
        )
        obj.ocupado = bool(dados.get("ocupado", False))
        return obj

    # ------------------------------------------------------------------
    # Representação
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"Atendente(id={self.id_atendente!r}, nome={self.nome!r}, "
            f"ocupado={self.ocupado})"
        )

    def __str__(self) -> str:
        status = " [OCUPADO]" if self.ocupado else " [LIVRE]"
        return f"[{self.id_atendente}] {self.nome}{status}"