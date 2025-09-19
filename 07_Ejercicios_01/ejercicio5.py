"""
Ejercicio 5. Hacer un programa que muestre todos los numeros entre dos
numeros que diga el usuario
"""

num1 = int(input("Introduce el primer número. \n"))
num2 = int(input("Introduce el segundo número. \n"))

if num1 < num2:
    string = str()
    for i in range(num1,num2+1):
        string += str(i) + " "
    print(string)
else:
    print("El número 1 debe ser menor que el número 2")