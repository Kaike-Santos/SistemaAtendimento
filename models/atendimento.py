# models/atendimento.py
# Classe Atendimento com registro de data, duração e atendente.

from datetime import datetime


class Atendimento:
    """Registra um atendimento finalizado."""

    def __init__(
        self,
        id_atendimento: str,
        id_cliente: str,
        id_atendente: str,
        data_hora: datetime | None = None,
        duracao_segundos: int = 0,
    ) -> None:
        self.id_atendimento = id_atendimento
        self.id_cliente = id_cliente
        self.id_atendente = id_atendente
        self.data_hora = data_hora or datetime.now()
        self.duracao_segundos = duracao_segundos

    # ------------------------------------------------------------------
    # Serialização
    # ------------------------------------------------------------------

    def para_dict(self) -> dict:
        return {
            "id_atendimento": self.id_atendimento,
            "id_cliente": self.id_cliente,
            "id_atendente": self.id_atendente,
            "data_hora": self.data_hora.isoformat(),
            "duracao_segundos": self.duracao_segundos,
        }

    @classmethod
    def de_dict(cls, dados: dict) -> "Atendimento":
        return cls(
            id_atendimento=dados["id_atendimento"],
            id_cliente=dados["id_cliente"],
            id_atendente=dados["id_atendente"],
            data_hora=datetime.fromisoformat(dados["data_hora"]),
            duracao_segundos=int(dados.get("duracao_segundos", 0)),
        )

    # ------------------------------------------------------------------
    # Representação
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"Atendimento(id={self.id_atendimento!r}, "
            f"cliente={self.id_cliente!r}, atendente={self.id_atendente!r}, "
            f"duracao={self.duracao_segundos}s)"
        )

    def __str__(self) -> str:
        minutos, segundos = divmod(self.duracao_segundos, 60)
        data_fmt = self.data_hora.strftime("%d/%m/%Y %H:%M")
        return (
            f"[{self.id_atendimento}] Cliente {self.id_cliente} | "
            f"Atendente {self.id_atendente} | "
            f"{data_fmt} | Duração: {minutos}min {segundos}s"
        )