import pytest, sys

def funcao():
	'''...'''

	sys.exit(1)

def test_funcao():
	with pytest.raises(SystemExit):
		funcao()
