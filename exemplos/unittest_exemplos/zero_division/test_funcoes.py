import unittest
from funcoes import soma
from funcoes import divisao

class TestFuncoes(unittest.TestCase):

	def test_soma_dois_inteiros(self):
		'''
		Verificar o valor de retorno da função
		passados dois números inteiros
		'''
		self.assertEqual(soma(1,1),2)
		self.assertEqual(soma(2,1),3)
		self.assertEqual(soma(2,2),4)

	def test_tipo_de_parametro(self):
		'''
		Verificar se a função lança um TypeError
		quando um tipo não suportado é passado
		'''
		self.assertRaises(TypeError,soma,'2','2')	
		self.assertRaises(TypeError,soma,2,'2')	
		self.assertRaises(TypeError,soma,'2',2)	
		self.assertRaises(TypeError,soma,2,True)	
		self.assertRaises(TypeError,soma,2,1+2j)
		self.assertRaises(TypeError,soma,1+2j,2)
		self.assertRaises(TypeError,soma,False,2)
		self.assertRaises(TypeError,soma,2.5,2)
		self.assertRaises(TypeError,soma,2,1.4)
			
	def test_divisao_por_zero(self):
		'''
		Verificar se a função retorna um ZeroDivisionError
		quando o denominador passado for zero
		'''
		self.assertRaises(ZeroDivisionError,divisao,2,0)
