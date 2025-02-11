class GotCharacter:
	def __init__(self, first_name, is_alive=True):
		if len(first_name) > 0:
			self.fist_name = first_name
		else:
			print("First name can't be empty")
		self.is_alive=is_alive

class Stark(GotCharacter):
	"""
    A class representing a member of the Stark family from Game of Thrones.

    Attributes:
        first_name (str): The first name of the character.
        is_alive (bool): A boolean indicating if the character is alive. Default is True.
        family_name (str): The family name of the character. For Stark, it is 'Stark'.
        house_words (str): The house words of the Stark family. Default is 'Winter is Coming'.

    Methods:
        print_house_words(): Prints the house words of the Stark family.
        die(): Changes the character's is_alive attribute to False, indicating death.
    """

	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name,is_alive=is_alive)
		self.family_name = "Stark"
		self.house_words = "Winter is Coming"

	def print_house_words(self):
		print(self.house_words)

	def die(self):
		self.is_alive=False

arya = Stark("Arya")
print(arya.__dict__)
arya.print_house_words()
print("Is Arya alive?", arya.is_alive)
arya.die()
print("Is Arya alive?", arya.is_alive)
