# tests/test_models.py

import unittest
from datetime import datetime
from models.cliente import Cliente
from models.atendente import Atendente
from models.atendimento import Atendimento


class TestCliente(unittest.TestCase):

    def test_criacao_valida(self):
        c = Cliente("001", "Ana", "11999990000", False)
        self.assertEqual(c.id_cliente, "001")
        self.assertFalse(c.prioridade)

    def test_validar_id_vazio(self):
        with self.assertRaises(ValueError):
            Cliente.validar_id("   ")

    def test_validar_telefone_curto(self):
        with self.assertRaises(ValueError):
            Cliente.validar_telefone("123")

    def test_validar_prioridade_string(self):
        self.assertTrue(Cliente.validar_prioridade("sim"))
        self.assertFalse(Cliente.validar_prioridade("nao"))

    def test_serializacao(self):
        c = Cliente("002", "Bruno", "11988887777", True)
        d = c.para_dict()
        c2 = Cliente.de_dict(d)
        self.assertEqual(c.id_cliente, c2.id_cliente)
        self.assertTrue(c2.prioridade)


class TestAtendente(unittest.TestCase):

    def test_criacao(self):
        a = Atendente("A01", "Carlos")
        self.assertFalse(a.ocupado)

    def test_nome_vazio(self):
        with self.assertRaises(ValueError):
            Atendente.validar_nome("")

    def test_serializacao(self):
        a = Atendente("A02", "Diana")
        a.ocupado = True
        d = a.para_dict()
        a2 = Atendente.de_dict(d)
        self.assertTrue(a2.ocupado)


class TestAtendimento(unittest.TestCase):

    def test_criacao(self):
        at = Atendimento("AT001", "001", "A01", duracao_segundos=120)
        self.assertEqual(at.duracao_segundos, 120)

    def test_serializacao(self):
        now = datetime(2025, 6, 1, 10, 0, 0)
        at = Atendimento("AT002", "002", "A02", data_hora=now, duracao_segundos=90)
        d = at.para_dict()
        at2 = Atendimento.de_dict(d)
        self.assertEqual(at2.id_cliente, "002")
        self.assertEqual(at2.duracao_segundos, 90)


if __name__ == "__main__":
    unittest.main()