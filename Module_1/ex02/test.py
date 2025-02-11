from vector import Vector
import sys
from pprint import pprint
import numpy as np
import typing

A = Vector([[1.], [2.], [3.]])
B = Vector([[4.], [5.], [6.]])
C = Vector([1., 2., 3.])
D = Vector([4., 5., 6.])
print(A)
print(B)
print(C)
print(D)

pprint(A.dot(B))
pprint(C.dot(D))
pprint(A.dot(C))
pprint(D.dot(A))

C.T()
pprint(C.__dict__)
C.T()
pprint(C.__dict__)
pprint(A+"test")
print("add")
print(A+B)
print(C+D)
print("sub")
print(A-B)
print(C-D)
print("division")
print(A/2)
print(C/2)
print(2/A)
print("multiplication")
print(A*2)
print(C*2)
print(2*A)
print(2*C)