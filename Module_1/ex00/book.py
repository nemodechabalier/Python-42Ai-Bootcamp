import sys
from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name):
        if len(name) > 0:
            self.name = name
        else:
            print("Book name cannot be empty.")
            sys.exit()

        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {
            "starter": [],
            "lunch": [],
            "dessert": []
        }

    def get_recipe_by_name(self, name):
        for recipes in self.recipes_list.values():
            for recipe in recipes:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        print("Recipe doesn't exist.")
        return None

    def get_recipes_by_types(self, recipe_type):
        if recipe_type in self.recipes_list:
            for recipe in self.recipes_list[recipe_type]:
                print(recipe)
        else:
            print("Invalid recipe type. Choose from: 'starter', 'lunch', 'dessert'")

    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            print("Invalid recipe type. Must be a Recipe instance.")
            return

        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()

    