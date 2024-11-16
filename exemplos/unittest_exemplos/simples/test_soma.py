import unittest
from funcoes import soma

class TestFuncoes(unittest.TestCase):

	def test_soma_dois_inteiros(self):
		'''
		Verificar o valor de retorno da função
		passados dois números inteiros
		'''
		self.assertEqual(soma(1,1),2)
		self.assertEqual(soma(2,1),3)
		self.assertEqual(soma(2,2),4)
