def ft_filter(function_to_apply, iterable):
    if not callable(function_to_apply):
        print("function_to_apply is not a function")
        return None
    try:
       iter(iterable)
    except TypeError:
        print("iterable is not iterable")
        return None
    
    for item in iterable:
        if function_to_apply(item):
            yield item


x = [1, 2, 3, 4, 5]
gen = ft_filter(lambda dum: dum % 2 == 0, x)

print(gen)  # Affiche quelque chose comme <generator object ft_filter at 0x7fab62ec18c0>

print(list(gen))  # Affiche [2, 4]

