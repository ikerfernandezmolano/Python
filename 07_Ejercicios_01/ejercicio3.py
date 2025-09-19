"""
Ejercicio 3. Imprimir los cuadrados de los primeros
             60 números naturales
"""

print("Con el bucle for")
for i in range(1,61):
    print(f"{i**2}")

print("\nCon el bucle while")
cont = 0
while cont <= 60:
    print(f"{cont**2}")
    cont += 1
