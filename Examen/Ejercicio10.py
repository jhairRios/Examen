import os
os.system('cls' if os.name == 'nt' else 'clear')

opcion ="S"

print(f"PIZZERIA BELLA NAPOLI")
print("PIZZAS DISPONIBLES")
print("1. VEGETARIANA")
print("2. No VEGETARIANA")
print("Desea su pizzsa vegetariana: ")
opcion = input()

while opcion.upper() == "S":
    print("Pizza Vegetariana")
    print("ingredientes")
    print("Pepino y tofu")     
else:
     print("Pizza No Vegetariana")
     print("Ingredientes")
     print("Peperoni, Jamon y Salmon")      
       