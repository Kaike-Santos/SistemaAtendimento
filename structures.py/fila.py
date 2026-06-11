# structures/fila.py
# Fila comum FIFO para atendimentos normais — O(1) enqueue/dequeue.

from collections import deque


class Fila:
    """
    Fila simples FIFO usando collections.deque.
    Enqueue: O(1). Dequeue: O(1). Peek: O(1).
    """

    def __init__(self) -> None:
        self._dados: deque = deque()

    def enqueue(self, cliente) -> None:
        """Adiciona cliente ao final da fila."""
        self._dados.append(cliente)

    def dequeue(self):
        """Remove e retorna o primeiro cliente. Retorna None se vazia."""
        if self.vazia():
            return None
        return self._dados.popleft()

    def peek(self):
        """Retorna o primeiro cliente sem remover."""
        if self.vazia():
            return None
        return self._dados[0]

    def vazia(self) -> bool:
        return len(self._dados) == 0

    def listar(self) -> list:
        return list(self._dados)

    def __len__(self) -> int:
        return len(self._dados)