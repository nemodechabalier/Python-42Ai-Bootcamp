import numpy as np

class NumPyCreator:
	def __init__(self):
		pass
	 
	def from_list(self, lst):
		try:
			array = np.array(lst)
			return array
		except Exception as e:
			print(f"Erreur lors de la conversion : {e}")
			return lst
	
	def from_tuple(self, tpl):
		try:
			array = np.array(tpl)
			return array
		except Exception as e:
			print(f"Erreur lors de la conversion : {e}")
			return tpl
	
	def from_iterable(self, itr):
		try:
			array = np.array(itr)
			return array
		except Exception as e:
			print(f"Erreur lors de la conversion : {e}")
			return itr

	def from_shape(self, shape, value=0):
			return np.full(shape, value)

	def random(self, shape):
		return np.random.rand(*shape)
	
	def identity(self, n):
		try :
			n = int(n)
		except ValueError:
			return
		return np.eye(n)

numpy = NumPyCreator()
lst = [1, 2, 3, 4, 5]
print(numpy.from_list(lst))
tup = (1, 2, 3, 4, 5)
print(numpy.from_tuple(tup))
s = {1, 2, 3, 4, 5}
d = {'a': 1, 'b': 2}
print(numpy.from_iterable(s))
print(numpy.from_iterable(d))
array1 = numpy.from_shape((2, 3), 5)
print(array1)

array2 = numpy.from_shape((3, 4))
print(array2)
array1 = numpy.random((2, 3))
print(array1)

array2 = numpy.random((3, 4))
print(array2)

matrix1 = numpy.identity(3)
print(matrix1)

matrix2 = numpy.identity(5)
print(matrix2)