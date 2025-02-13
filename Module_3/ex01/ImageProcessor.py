from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt


class ImageProcessor:

	def __init__(self):
		pass

	def load(self,path):
		if not isinstance(path, str):
			return
		if not os.path.exists(path):
			print(f"Erreur : Le fichier '{path}' n'existe pas.")
			return None
		try:
			image = Image.open(path)
			img_array = np.array(image)
			print(f"Dimensions de l'image : {img_array.shape[0]} x {img_array.shape[1]}")
			return img_array
		except Exception as e:
			print(f"Erreur lors de la lecture de l'image : {e}")
			return None
		
	def display(self, array):
		if array is not None:
			plt.imshow(array)
			plt.axis('off')
			plt.show()
		else:
			print("Erreur : L'image n'a pas pu être chargée.")

imp = ImageProcessor()
arr = imp.load("non_existing_file.png")
print(arr)
arr = imp.load("ressources/42AIlogo.png")
print(arr)
imp.display(arr)