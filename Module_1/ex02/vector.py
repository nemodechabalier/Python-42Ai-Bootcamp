import sys
from pprint import pprint
import numpy as np
import typing

class Vector:
	def __init__(self, values:list):
		if isinstance(values, list) and all(isinstance(i, list) for i in values):
			for element in values:
				for nb in element:
					try:
						nb = float(nb)
					except ValueError:
						print("Error not a int or float")
						sys.exit()
			self.shape = [len(values), 1]
			self.values = np.array(values)

		elif isinstance(values, list):
			for nb in values :
				try:
					nb = float(nb)
				except ValueError:
					print("Error not a int or float")
					sys.exit()
			self.shape = [1, len(values)]
			self.values = np.array(values)

	def dot(self, vector) -> float:
		if not isinstance(vector, Vector):
			print("dot: not a vector")
			return None
		if len(self.values) != len(vector.values):
			print("dot: not the same dimension or type of vector")
			return None
		if self.shape[0] == 1 and vector.shape[0] == 1:
			dot_product = sum(self.values[i] * vector.values[i] for i in range(len(self.values)))
		elif self.shape[1] == 1 and vector.shape[1] == 1:
			dot_product = sum(self.values[i][0] * vector.values[i][0] for i in range(len(self.values)))
		
		elif self.shape[0] == 1:
			dot_product = sum(self.values[i] * vector.values[i][0] for i in range(len(self.values)))
		else:
			dot_product = sum(self.values[i][0] * vector.values[i] for i in range(len(self.values)))
		return dot_product

	def T(self):
		if self.shape[0] == 1:
			self.values = np.array(self.values).reshape(-1, 1)
			self.shape[0] = self.shape[1]
			self.shape[1] = 1
		else:
			self.values = np.array(self.values).reshape(-1)
			self.shape[1] = self.shape[0]
			self.shape[0] = 1

	def __str__(self):
		return f"Vector(shape={self.shape}, values={self.values})"

	def __add__(self, other: 'Vector') -> 'Vector':
		if not isinstance(other, Vector):
			print("add: not a vector")
			return None
		if self.shape != other.shape:
			print("Error not same shape")
			return None
		elif self.shape[1] == 1:
			value = [[self.values[i][0] + other.values[i][0]] for i in range(self.shape[0])]
			return Vector(value)
		else :
			value = [self.values[i] + other.values[i] for i in range (self.shape[1])]
			return Vector(value)
		
	def __radd__(self, other: 'Vector') -> 'Vector':
		return self.__add__(other)
	
	def __sub__(self, other: 'Vector') -> 'Vector':
		if not isinstance(other, Vector):
			print("add: not a vector")
			return None
		if self.shape != other.shape:
			print("Error not same shape")
			return None
		elif self.shape[1] == 1:
			value = [[self.values[i][0] - other.values[i][0]] for i in range(self.shape[0])]
			return Vector(value)
		else :
			value = [self.values[i] - other.values[i] for i in range (self.shape[1])]
			return Vector(value)
		
	def __rsub__(self, other: 'Vector') -> 'Vector':
		return self.__sub__(other)

	def __mul__(self, nb:int):
		try:
			nb = int(nb)
		except ValueError:
			print("not a int")
			return None
		if self.shape[1] == 1:
			value = [[self.values[i][0] * nb] for i in range(self.shape[0])]
			return Vector(value)
		else :
			value = [self.values[i] * nb for i in range (self.shape[1])]
			return Vector(value)
	def __rmul__(self, nb:int):
		try:
			nb = int(nb)
		except ValueError:
			print("not a int")
			return None
		return self.__mul__(nb)
	def __truediv__(self, nb:int):
		try:
			nb = int(nb)
		except ValueError:
			print("not a int")
			return None
		if self.shape[1] == 1:
			value = [[self.values[i][0] / nb] for i in range(self.shape[0])]
			return Vector(value)
		else :
			value = [self.values[i] / nb for i in range (self.shape[1])]
			return Vector(value)
	def __rtruediv__(self, nb:int):
		print("NotImplementedError: Division of a scalar by a Vector is not defined here.")
		NotImplemented
