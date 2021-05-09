def soma(x,y):
	'''
	Função que soma dois inteiros x e y
	:param x: int
	:param y: int
	'''
	if type(x) not in [int]:
		raise TypeError("x e y devem ser do tipo int")
	elif type(y) not in [int]:
		raise TypeError("x e y devem ser do tipo int")
	return x+y

def divisao(x,y):
	'''
	Função que divide x por y
	:param x: float
	:param y: float
	'''
	if y==0:
		raise ZeroDivisionError("y não pode ser zero!")
	return x/y
