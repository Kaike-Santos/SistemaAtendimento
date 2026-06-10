# models/cliente.py
# Classe Cliente com validações de negócio.


class Cliente:
    """Representa um cliente cadastrado no sistema."""

    def __init__(
        self,
        id_cliente: str,
        nome: str,
        telefone: str,
        prioridade: bool = False,
    ) -> None:
        self.id_cliente = id_cliente
        self.nome = nome
        self.telefone = telefone
        self.prioridade = prioridade  # True = atendimento prioritário

    # ------------------------------------------------------------------
    # Validações
    # ------------------------------------------------------------------

    @staticmethod
    def validar_id(valor: str) -> str:
        valor = valor.strip()
        if not valor:
            raise ValueError("ID não pode ser vazio.")
        return valor

    @staticmethod
    def validar_nome(valor: str) -> str:
        valor = valor.strip()
        if not valor:
            raise ValueError("Nome não pode ser vazio.")
        return valor

    @staticmethod
    def validar_telefone(valor: str) -> str:
        digitos = "".join(filter(str.isdigit, valor))
        if len(digitos) < 8:
            raise ValueError("Telefone inválido (mínimo 8 dígitos).")
        return valor.strip()

    @staticmethod
    def validar_prioridade(valor: str | bool) -> bool:
        if isinstance(valor, bool):
            return valor
        return str(valor).strip().lower() in ("true", "1", "sim", "s")

    # ------------------------------------------------------------------
    # Serialização
    # ------------------------------------------------------------------

    def para_dict(self) -> dict:
        return {
            "id_cliente": self.id_cliente,
            "nome": self.nome,
            "telefone": self.telefone,
            "prioridade": self.prioridade,
        }

    @classmethod
    def de_dict(cls, dados: dict) -> "Cliente":
        return cls(
            id_cliente=dados["id_cliente"],
            nome=dados["nome"],
            telefone=dados["telefone"],
            prioridade=bool(dados.get("prioridade", False)),
        )

    # ------------------------------------------------------------------
    # Representação
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"Cliente(id={self.id_cliente!r}, nome={self.nome!r}, "
            f"telefone={self.telefone!r}, prioridade={self.prioridade})"
        )

    def __str__(self) -> str:
        prio = " [PRIORITÁRIO]" if self.prioridade else ""
        return f"[{self.id_cliente}] {self.nome} | {self.telefone}{prio}"