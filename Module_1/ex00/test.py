from book import Book
from recipe import Recipe

book = Book("Mon super book")
Recipe1 =  Recipe("pate", 1, 11 ,"pate", "", "lunch")
Recipe2 = Recipe("pate au beurre", 1, 10,"pate beurre", "", "lunch")
book.add_recipe(repice1)
book.add_recipe(repice2)
book.get_recipe_by_name("pate")
book.get_recipes_by_types("pate")
book.get_recipes_by_types("lunch")


