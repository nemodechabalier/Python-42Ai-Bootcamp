import time
import os
from random import randint

# Décorateur @log
def log(func):
    def wrapper(*args, **kwargs):
        username = os.getenv('USER', 'Unknown User')
        
        start_time = time.time()
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        exec_time = round((end_time - start_time) * 1000, 3)  # En millisecondes
        
        method_name = func.__name__.replace('_', ' ').title()  # Remplacer les underscores par des espaces et mettre en titre
        log_entry = f"({username})Running: {method_name:<16} [ exec-time = {exec_time} ms ]"
        
        with open("machine.log", "a") as log_file:
            log_file.write(log_entry + '\n')
        
        return result

    return wrapper

class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
        return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

# Exemple d'utilisation
if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
        machine.make_coffee()
    machine.add_water(70)
