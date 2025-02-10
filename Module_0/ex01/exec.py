import sys

argument = sys.argv[1:]
if (len(argument) < 1):
	sys.exit()
reversed_words = [word[::-1] for word in argument]
print (" ".join(reversed(reversed_words)).swapcase())

