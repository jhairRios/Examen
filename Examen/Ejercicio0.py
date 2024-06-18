import os
os.system('cls' if os.name == 'nt' else 'clear')

precio = 10
edad = 0


print(f"TIENDA DE JUEGOS")
print("Ingrese la edad del cliente: ")
edad = int(input())

if(edad >= 5):
    print("El usuario deve pagar L.10")
elif(edad <= 4):
    print ("El usuario entra gratis")
print("Desae ingresar otro cliente: ")


    