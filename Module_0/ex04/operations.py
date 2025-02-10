import sys

def operation( nb1, nb2):
	print("Sum:        ", nb1 + nb2, "\nDifference: ", nb1 - nb2 ,"\nProduct:    ", nb1 * nb2)
	if nb2 == 0:
		print ("Quotient:   ERROR (division by zero)\nRemainder:  ERROR (modulo by zero)")
	else :
		print ("Quotient:   ", nb1 / nb2, "\nRemainder:  ", nb1 % nb2,)


argument = sys.argv[1:]

if len(argument) == 0 or len(argument) == 1:
	print ("Usage: python operations.py <number1> <number2>\nExample:\npython operations.py 10 3")
	sys.exit()
if len(argument) > 2:
	print("AssertionError: too many arguments")
	sys.exit()
try :
	nb1 = int(argument[0])
	nb2 = int(argument[1])
	operation(nb1,nb2)
except ValueError:
	print("AssertionError: only integers")