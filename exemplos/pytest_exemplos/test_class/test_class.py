class TestClass:

	value = 10

	def test_primeiro(self):
		self.value = 11
		assert self.value == 11
		name = "Geofisicando"
		assert name == "Geofisicando"
	def test_segundo(self):
		assert self.value == 11
		assert 1 == 1
		assert 2 != 3

class TestNova:
	def test_terceiro(self):
		assert 4 == 4
