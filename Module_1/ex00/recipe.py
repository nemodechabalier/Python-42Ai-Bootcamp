import sys

class Recipe:

	def __init__(self,name,cooking_lvl,cooking_time,ingredients,description,recipe_type):
		if len(name) > 0:
			self.name = name
		else:
			print ("Name can't be empty")
			sys.exit()
		try :
			nb = int(cooking_lvl)
			self.cooking_lvl = cooking_lvl
		except ValueError or nb > 5 or nb < 1:
			print("cooking_lvl have to be int")
			sys.exit()
		try :
			nb = int(cooking_time)
			self.cooking_time = nb
		except ValueError or nb < 0:
			print("cooking_time have to be int")
			sys.exit()
		if len(ingredients) > 0:
			self.ingredients = ingredients
		else:
			print ("ingredients can't be empty")
			sys.exit()

		self.description = description

		if recipe_type == "starter" or recipe_type == "lunch" or recipe_type == "dessert":
			self.recipe_type = recipe_type
		else :
			print("recipe_type can be 'starter', 'lunch' or 'dessert'")
			sys.exit()

	def __str__(self):
		return (
        	f"{self.name}\n"
        	f"The cooking level is: {self.cooking_lvl}\n"
        	f"Time you need: {self.cooking_time} minutes\n"
        	f"Ingredients: {', '.join(self.ingredients)}\n"
        	f"Description: {self.description}\n"
        	f"Type: {self.recipe_type}\n"
    	)
