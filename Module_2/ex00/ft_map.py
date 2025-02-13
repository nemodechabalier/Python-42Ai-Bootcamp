def ft_map(function_to_apply, iterable):
    if not callable(function_to_apply):
        print("function_to_apply is not a function")
        return iter([]) 
    try:
        iter(iterable)
    except TypeError:
        print("iterable is not iterable")
        return iter([]) 

    for item in iterable:
        yield function_to_apply(item)


# Fonction de test
def square(x):
    return x * x

# Test 1 : Liste de nombres
lst = [1, 2, 3, 4, 5]
print(list(ft_map(square, lst)))  # Doit afficher [1, 4, 9, 16, 25]

# Test 2 : Tuple de nombres
tpl = (10, 20, 30)
print(list(ft_map(lambda x: x / 2, tpl)))  # Doit afficher [5.0, 10.0, 15.0]

# Test 3 : Chaîne de caractères (doit échouer avec une fonction non adaptée)
print(list(ft_map(int, "12345")))  # Doit afficher [1, 2, 3, 4, 5]

# Test 4 : Iterable invalide
print(ft_map(square, None))  # Doit afficher None

# Test 5 : Fonction invalide
print(ft_map("not a function", [1, 2, 3]))  # Doit afficher None

x = [1, 2, 3, 4, 5]

# Appel de ft_map sans list(), ce qui renvoie un générateur
gen = ft_map(lambda dum: dum + 1, x)
print(gen)  # Affiche quelque chose comme <generator object ft_map at 0x7f708faab7b0>

# Conversion du générateur en liste
result = list(gen)
print(result)  # Affiche [2, 3, 4, 5, 6]
