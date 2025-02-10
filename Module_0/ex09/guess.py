import random
import sys

print ("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!\n")
n = random.randint(1,99)
attempt = 0
while (1):
	print("What's your guess between 1 and 99?")
	str = input(">> ")
	if (str == "exit"):
		sys.exit()
	try:
		attempt += 1
		nb = int(str)
		if nb == 42 and attempt == 1:
			print("The answer to the ultimate question of life, the universe and everything is 42.\nCongratulations! You got it on your first try!")
			sys.exit()
		if nb == n:
			print("Congratulations, you've got it!")
			print("You won in ", attempt, " attempts!")
			sys.exit()
		elif nb > n:
			print("Too high!")
		else:
			print("Too low!")
	except ValueError:
		print("That's not a number.")
