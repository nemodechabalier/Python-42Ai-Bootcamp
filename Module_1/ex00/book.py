import sys
from datetime import datetime
from recipe import Recipe

class Book:
	def __init__(self,name):
		if len(name) > 0 :
			self.name = name
		else:
			sys.exit()
		self.last_update = datetime.now()
		self.creation_date = datetime.now()
		self.recipes_list = {
            "starter": [],
            "lunch": [],
            "dessert": []
        }
		self.recipe = []

	def get_recipe_by_name(self, name):
		if self.recipe[name]:
			print(self.recipe[name].__str__())
		else :	
			print("recipe don't existe")
		return this

	def get_recipes_by_types(self, recipe_type):
		if recipe_type == "starter" or recipe_type == "lunch" or recipe_type == "dessert":
			for word in recipes_list[recipe_type]:
				print(self.recipe[word].__str__())
		else :
			print("It's not a recipe_type")

	def add_recipe(self, recipe):
		self.recipe.append(recipe)
		self.recipes_list[].apend()
		self.last_update = datetime.now()

	