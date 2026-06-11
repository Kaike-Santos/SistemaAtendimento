# structures/vetor_ordenado.py
# Vetor ordenado por id com busca binária — O(log n) na busca.
# Inserção mantém a ordem: O(n). Remoção: O(n).


class VetorOrdenado:
    """
    Vetor ordenado por id_cliente.
    Busca binária garante O(log n) para encontrar clientes.
    Inserção ordenada garante O(n) no pior caso.
    """

    def __init__(self) -> None:
        self._dados: list = []

    # ------------------------------------------------------------------
    # Inserção ordenada — O(n)
    # ------------------------------------------------------------------

    def inserir(self, cliente) -> None:
        """Insere mantendo a ordem crescente por id_cliente."""
        pos = 0
        while pos < len(self._dados) and self._dados[pos].id_cliente < cliente.id_cliente:
            pos += 1
        self._dados.insert(pos, cliente)

    # ------------------------------------------------------------------
    # Busca binária — O(log n)
    # ------------------------------------------------------------------

    def buscar(self, id_cliente: str):
        """Retorna o cliente com o id informado ou None."""
        esq, dir_ = 0, len(self._dados) - 1
        while esq <= dir_:
            meio = (esq + dir_) // 2
            atual = self._dados[meio].id_cliente
            if atual == id_cliente:
                return self._dados[meio]
            elif atual < id_cliente:
                esq = meio + 1
            else:
                dir_ = meio - 1
        return None

    # ------------------------------------------------------------------
    # Remoção — O(n)
    # ------------------------------------------------------------------

    def remover(self, id_cliente: str) -> bool:
        """Remove o cliente pelo id. Retorna True se removido."""
        cliente = self.buscar(id_cliente)
        if cliente:
            self._dados.remove(cliente)
            return True
        return False

    def listar(self) -> list:
        return list(self._dados)

    def __len__(self) -> int:
        return len(self._dados)