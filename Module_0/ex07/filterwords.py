import sys
import string

def print_word(str,nb):
	lst = []
	for char in string.punctuation:
		str.replace(char," ")
	words = str.split()
	for word in words:
		if len(word) > nb and word not in lst:
			lst.append(word)
	print(lst)


arguments = sys.argv[1:]
if len(arguments) != 2:
	print("Error")
	sys.exit()
try:
	nb = int(arguments[1])
	print_word(arguments[0],nb)
except ValueError:
	print("Error")