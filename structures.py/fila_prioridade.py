# structures/fila_prioridade.py
# Fila de prioridade: clientes prioritários na frente, ordem de chegada preservada.
# Inserção: O(1). Dequeue: O(n) para encontrar o primeiro prioritário, depois O(1).


class FilaPrioridade:
    """
    Fila que respeita prioridade e ordem de chegada.
    Clientes com prioridade=True ficam antes dos demais,
    mas a ordem de chegada é preservada dentro de cada grupo.
    Enqueue: O(1). Dequeue: O(n).
    """

    def __init__(self) -> None:
        self._fila_prioritaria: list = []
        self._fila_normal: list = []

    def enqueue(self, cliente) -> None:
        """Insere na fila correta conforme prioridade."""
        if cliente.prioridade:
            self._fila_prioritaria.append(cliente)
        else:
            self._fila_normal.append(cliente)

    def dequeue(self):
        """
        Remove o próximo cliente.
        Prioritários saem primeiro; dentro de cada grupo, FIFO.
        """
        if self._fila_prioritaria:
            return self._fila_prioritaria.pop(0)
        if self._fila_normal:
            return self._fila_normal.pop(0)
        return None

    def peek(self):
        """Retorna o próximo sem remover."""
        if self._fila_prioritaria:
            return self._fila_prioritaria[0]
        if self._fila_normal:
            return self._fila_normal[0]
        return None

    def vazia(self) -> bool:
        return not self._fila_prioritaria and not self._fila_normal

    def listar(self) -> list:
        """Retorna a fila completa: prioritários primeiro, depois normais."""
        return list(self._fila_prioritaria) + list(self._fila_normal)

    def __len__(self) -> int:
        return len(self._fila_prioritaria) + len(self._fila_normal)