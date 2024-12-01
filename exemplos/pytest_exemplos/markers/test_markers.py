import pytest

@pytest.mark.geofisicando
def test_qualquer():
	assert 1 == 1

@pytest.mark.skip
def test_para_pular():
	assert 2 == 1

@pytest.mark.xfail
def test_que_vai_falhar():
	assert 2 == 1
