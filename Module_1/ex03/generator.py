import random

def generator(text, sep, option=None):
	if not isinstance(text,str) or not isinstance(sep,str):
		print("Error")
		return None
	if option != "shuffle" and option != "unique" and option != "ordered" and option !=None:
		print("Error")
		return None
	split = text.split(sep)

	if option == "shuffle":
		random.shuffle(split)
	elif option == "unique":
		split = list(set(split))
	elif option == "ordered":
		split = sorted(split)
	for word in split:
		yield word

text = "Le Lorem Ipsum est simplement du faux texte."

print("no option:\n")
for word in generator(text, sep=" "):
	print(word)
print("\nshuffle:\n")
for word in generator(text, sep=" ", option="shuffle"):
	print(word)
print("\nordered:\n")
for word in generator(text, sep=" ", option="ordered"):
	print(word)
print("\nunique:\n")
text = "Lorem Ipsum Lorem Ipsum"
for word in generator(text, sep=" ", option="unique"):
	print(word)
print("\nError:\n")
text = 1.0
for word in generator(text, sep=" "):
	print(word)