# structures/pilha.py
# Pilha LIFO para desfazer a última finalização de atendimento.
# Push: O(1). Pop: O(1). Peek: O(1).


class Pilha:
    """
    Pilha LIFO.
    Push: O(1). Pop: O(1). Peek: O(1).
    Usada para desfazer a última finalização de atendimento.
    """

    def __init__(self) -> None:
        self._dados: list = []

    def push(self, item) -> None:
        """Empilha um item."""
        self._dados.append(item)

    def pop(self):
        """Desempilha e retorna o topo. Retorna None se vazia."""
        if self.vazia():
            return None
        return self._dados.pop()

    def peek(self):
        """Retorna o topo sem remover."""
        if self.vazia():
            return None
        return self._dados[-1]

    def vazia(self) -> bool:
        return len(self._dados) == 0

    def __len__(self) -> int:
        return len(self._dados)