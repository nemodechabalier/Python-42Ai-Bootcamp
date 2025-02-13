def what_are_the_vars(*args, **kwargs):
    # Créer une instance de la classe ObjectC
    obj = ObjectC()
    
    # Ajouter les arguments positionnels comme attributs
    for i, arg in enumerate(args):
        setattr(obj, f"var_{i}", arg)
    
    # Ajouter les arguments nommés comme attributs
    for key, value in kwargs.items():
        setattr(obj, key, value)
    
    return obj

class ObjectC(object):
    pass

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':  # Ignorer les attributs privés (qui commencent par _)
            value = getattr(obj, attr)
            print(f"{attr}: {value}")
    print("end")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    
    obj = what_are_the_vars()
    doom_printer(obj)
    
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
