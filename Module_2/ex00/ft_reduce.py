def ft_reduce(function_to_apply, iterable):
    if not callable(function_to_apply):
        print("function_to_apply is not a function")
        return None
    
    try:
        iter(iterable)
    except TypeError:
        print("iterable is not iterable")
        return None
    
    try:
        iterator = iter(iterable)
        result = next(iterator)
    except StopIteration:
        return None
    
    for item in iterator:
        result = function_to_apply(result, item)
    return result



lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(ft_reduce(lambda u, v: u + v, lst)) #"Hello world"

x = [1, 2, 3, 4]

sum_result = ft_reduce(lambda a, b: a + b, x)
print(sum_result)  # Affiche 10 (1 + 2 + 3 + 4)

product_result = ft_reduce(lambda a, b: a * b, x)
print(product_result)  # Affiche 24 (1 * 2 * 3 * 4)

empty_result = ft_reduce(lambda a, b: a + b, [])
print(empty_result)  # Affiche None
