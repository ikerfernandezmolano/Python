"""
Ejercicio 9. Hacer un programa que pida numeros al usuario
indefinadamente hasta meter el número 111
"""

num = -1
while num != 111:
    num = int(input("Introduce un número: "))

for i in range(10000):
    num = int(input("Introduce un número: "))
    if num == 111:
        break