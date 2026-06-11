# tests/test_business.py

import unittest
from unittest.mock import MagicMock

from structures.fila_prioridade import FilaPrioridade
from business import regras_fila


def _cliente(id_: str, prio: bool = False):
    c = MagicMock()
    c.id_cliente = id_
    c.prioridade = prio
    return c


class TestRegrasFila(unittest.TestCase):

    def setUp(self):
        regras_fila._fila = FilaPrioridade()

    def test_entrar_e_chamar(self):
        regras_fila.entrar_na_fila(_cliente("001"))

        proximo = regras_fila.chamar_proximo()

        self.assertEqual(
            proximo.id_cliente,
            "001",
        )

    def test_fila_vazia_retorna_none(self):
        self.assertIsNone(
            regras_fila.chamar_proximo()
        )

    def test_prioridade_na_frente(self):
        regras_fila.entrar_na_fila(
            _cliente("N1", False)
        )

        regras_fila.entrar_na_fila(
            _cliente("P1", True)
        )

        proximo = regras_fila.chamar_proximo()

        self.assertEqual(
            proximo.id_cliente,
            "P1",
        )

    def test_tamanho_da_fila(self):
        regras_fila.entrar_na_fila(_cliente("001"))
        regras_fila.entrar_na_fila(_cliente("002"))

        self.assertEqual(
            regras_fila.tamanho_fila(),
            2,
        )


if __name__ == "__main__":
    unittest.main()