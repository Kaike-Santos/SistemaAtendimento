# tests/test_structures.py

import unittest
from unittest.mock import MagicMock
from structures.vetor_ordenado import VetorOrdenado
from structures.fila import Fila
from structures.fila_prioridade import FilaPrioridade
from structures.pilha import Pilha


def _cliente(id_: str, prio: bool = False):
    c = MagicMock()
    c.id_cliente = id_
    c.prioridade = prio
    return c


class TestVetorOrdenado(unittest.TestCase):

    def test_insercao_ordenada(self):
        v = VetorOrdenado()
        v.inserir(_cliente("003"))
        v.inserir(_cliente("001"))
        v.inserir(_cliente("002"))
        ids = [c.id_cliente for c in v.listar()]
        self.assertEqual(ids, ["001", "002", "003"])

    def test_busca_binaria_encontra(self):
        v = VetorOrdenado()
        v.inserir(_cliente("010"))
        v.inserir(_cliente("020"))
        resultado = v.buscar("010")
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.id_cliente, "010")

    def test_busca_binaria_nao_encontra(self):
        v = VetorOrdenado()
        v.inserir(_cliente("001"))
        self.assertIsNone(v.buscar("999"))

    def test_remocao(self):
        v = VetorOrdenado()
        v.inserir(_cliente("001"))
        self.assertTrue(v.remover("001"))
        self.assertEqual(len(v), 0)


class TestFila(unittest.TestCase):

    def test_enqueue_dequeue(self):
        f = Fila()
        f.enqueue(_cliente("A"))
        f.enqueue(_cliente("B"))
        self.assertEqual(f.dequeue().id_cliente, "A")

    def test_vazia(self):
        f = Fila()
        self.assertTrue(f.vazia())
        self.assertIsNone(f.dequeue())


class TestFilaPrioridade(unittest.TestCase):

    def test_prioridade_antes_normal(self):
        fp = FilaPrioridade()
        fp.enqueue(_cliente("N1", prio=False))
        fp.enqueue(_cliente("P1", prio=True))
        self.assertEqual(fp.dequeue().id_cliente, "P1")

    def test_ordem_dentro_do_grupo(self):
        fp = FilaPrioridade()
        fp.enqueue(_cliente("P1", prio=True))
        fp.enqueue(_cliente("P2", prio=True))
        self.assertEqual(fp.dequeue().id_cliente, "P1")

    def test_vazia(self):
        fp = FilaPrioridade()
        self.assertTrue(fp.vazia())
        self.assertIsNone(fp.dequeue())


class TestPilha(unittest.TestCase):

    def test_push_pop(self):
        p = Pilha()
        p.push("a1")
        p.push("a2")
        self.assertEqual(p.pop(), "a2")

    def test_pop_vazia(self):
        p = Pilha()
        self.assertIsNone(p.pop())

    def test_peek(self):
        p = Pilha()
        p.push("x")
        self.assertEqual(p.peek(), "x")
        self.assertEqual(len(p), 1)


if __name__ == "__main__":
    unittest.main()