"""
TDD - Test driven development (Desenvolvimento dirigido a testes)

Red
Parte 1 -> Criar o teste e ver falhar

Green
Parte 2 -> Criar o código e ver o teste passar

Refactor
Parte 3 -> Melhorar meu código
"""

import unittest
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent 
MODULE_PATH = ROOT_FOLDER / 'chocolatecomamendoim.py'
from chocolatecomamendoim import chocolate_com_amendoim


class TestChocolateComAmendoim(unittest.TestCase):
    def test_chocolate_com_amendoim_deve_levantar_assertion_error_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            chocolate_com_amendoim('')
    

    def test_chocolate_com_amendoim_deve_retornar_chocolate_com_amendoim_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Chocolate com Amendoim'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(chocolate_com_amendoim(entrada), saida, msg=f'"{entrada}" não retornou "{saida}"')
    
    def test_chocolate_com_amendoim_deve_retornar_passar_fome_se_entrada_nao_for_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 7, 8)
        saida = 'Passar fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(chocolate_com_amendoim(entrada), saida, msg=f'"{entrada}" não retornou "{saida}"')
    
    def test_chocolate_com_amendoim_deve_retornar_chocolate_se_entrada_for_multiplo_de_3(self):
        entradas = (3, 6, 9, 12, 18, 21)
        saida = 'Chocolate'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(chocolate_com_amendoim(entrada), saida, msg=f'"{entrada}" não retornou "{saida}"')
    
    def test_chocolate_com_amendoim_deve_retornar_amendoim_se_entrada_for_multiplo_de_5(self):
        entradas = (5, 10, 20, 25, 35)
        saida = 'Amendoim'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(chocolate_com_amendoim(entrada), saida, msg=f'"{entrada}" não retornou "{saida}"')
                


if __name__ == '__main__':
    unittest.main(verbosity=2)