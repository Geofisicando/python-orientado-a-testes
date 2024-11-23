import pytest

def soma(x,y):
	if type(x) not in [int] or type(y) not in [int]:
		raise TypeError("x e y precisam ser do tipo int!")
	return x+y

def test_raises_typeerror():
	with pytest.raises(TypeError):
		soma('1',2)
	with pytest.raises(TypeError):
		soma(1,'2')
	with pytest.raises(TypeError):
		soma('1','2')

	with pytest.raises(TypeError):
		soma(1,2)















