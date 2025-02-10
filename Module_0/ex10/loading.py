import time
import sys
from time import sleep

def ft_progress(lst):
    start_time = time.time()  # Démarrer le chronomètre
    total = len(lst)

    for i, elem in enumerate(lst, start=1):
        elapsed_time = time.time() - start_time  # Temps écoulé
        speed = elapsed_time / i  # Temps moyen par itération
        eta = speed * (total - i)  # Temps estimé restant

        percentage = (i / total) * 100  # Pourcentage de progression
        bar_length = 20  # Longueur de la barre
        filled_length = int(bar_length * i // total)  # Remplissage
        bar = "=" * filled_length + ">" + " " * (bar_length - filled_length)

        # Affichage de la barre
        sys.stdout.write(f"\rETA: {eta:.2f}s [{percentage:3.0f}%][{bar}] {i}/{total} | elapsed time {elapsed_time:.2f}s")
        sys.stdout.flush()

        yield elem  # Retourner l'élément pour la boucle for

    print()  # Nouvelle ligne après la fin de la boucle

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
	ret += elem
	sleep(0.005)
print()
print(ret)
