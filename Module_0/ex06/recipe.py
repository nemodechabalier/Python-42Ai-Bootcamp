import sys


def add():
    name = input(">>> Enter a name: ")
    while len(name) == 0:
        name = input(">>> Enter a name: ")

    cookbook[name] = {}

    ingredients = []

    print(">>> Enter ingredients :")
    while True:
        ingredient = input()
        if len(ingredient) == 0:
            break
        if len(ingredient) > 0:
            ingredients.append(ingredient)
    cookbook[name]['ingredients'] = ingredients

    type_meal = input(">>> Enter a meal type: ")
    while len(type_meal) == 0:
        type_meal = input(">>> Enter a meal type: ")
    cookbook[name]['meal'] = type_meal

    time = input(">>> Enter a preparation time: ")
    while not time.isdigit() or int(time) < 0:
        time = input(">>> Enter a valid preparation time : ")
    cookbook[name]['prep_time'] = int(time)
    print(f"Recipe for {name} has been added.")



def delete():
	what = input(">>> Enter a name: ")
	try:
		del cookbook[what]
	except KeyError:
		print(">>> ", what, "don't exist")

def recipe():
	idea = input(">>> Enter a name: ")
	try:
		print(cookbook[idea])
	except KeyError:
		print(">>> ", what, "don't exist")

def P_cookbook():
	print(cookbook)

def quite():
	print("Cookbook closed. Goodbye !")
	sys.exit()

cookbook = {
    "Sandwich": {
        'ingredients': ["ham", "bread", "cheese", "tomatoes"],
        'meal': 'lunch',
        'prep_time': 10,
    },
    "Cake": {
        'ingredients': ["flour", "sugar", "eggs"],
        'meal': 'desert',
        'prep_time': 60,
    },
    "Salad": {
        'ingredients': ["avocado", "aruyula", "tomatoes", "spinach"],
        'meal': 'lunch',
        'prep_time': 15,
    },
}
while (1):
	variable = input("Welcome to the Python Cookbook !\nList of available options:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n")
	try:
		nb = int(variable)
		if nb == 1:
			add()
		elif nb == 2:
			delete()
		elif nb == 3:
			recipe()
		elif nb == 4:
			P_cookbook()
		elif nb == 5:
			quite()
		else:
			print("Error Wrong Instruction!!")
	except ValueError:
		print("Error Wrong Instruction!!")

