# structures/lista_encadeada.py
# Lista encadeada simples para gerenciar clientes ativos.
# Inserção no início: O(1). Remoção: O(n). Busca: O(n). 


class No:
    """Nó da lista encadeada."""

    def __init__(self, cliente) -> None:
        self.cliente = cliente
        self.proximo: "No | None" = None


class ListaEncadeada:
    """
    Lista encadeada de clientes ativos.
    Inserção no início: O(1).
    Remoção por id: O(n).
    Busca por id: O(n).
    """

    def __init__(self) -> None:
        self._cabeca: No | None = None
        self._tamanho: int = 0

    def inserir(self, cliente) -> None:
        no = No(cliente)
        no.proximo = self._cabeca
        self._cabeca = no
        self._tamanho += 1

    def buscar(self, id_cliente: str):
        atual = self._cabeca
        while atual:
            if atual.cliente.id_cliente == id_cliente:
                return atual.cliente
            atual = atual.proximo
        return None

    def remover(self, id_cliente: str) -> bool:
        anterior = None
        atual = self._cabeca

        while atual:
            if atual.cliente.id_cliente == id_cliente:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self._cabeca = atual.proximo

                self._tamanho -= 1
                return True

            anterior = atual
            atual = atual.proximo

        return False

    def listar(self) -> list:
        resultado = []
        atual = self._cabeca

        while atual:
            resultado.append(atual.cliente)
            atual = atual.proximo

        return resultado

    def vazia(self) -> bool:
        return self._cabeca is None

    def __len__(self) -> int:
        return self._tamanho