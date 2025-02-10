import sys

argument = sys.argv[1:]

if (len(argument) < 1):
	sys.exit()
if (len(argument) > 1):
	print("AssertionError: more than one argument is provided")
	sys.exit()
try :
	argument = int(argument[0])
except ValueError:
	print("AssertionError: argument is not an integer")
	sys.exit()

if argument == 0:
	print ("I'm Zero.")
elif argument % 2 == 0:
	print("I'm Even.")
else:
	print("I'm Odd.")