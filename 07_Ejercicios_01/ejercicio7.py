"""
Ejercicio 7. Hacer un programa que muestre todos los numeros
impares entre dos números dados por el usuario
"""

parar = False 
while not parar:
    num1 = int(input("Introduce el primer número. \n"))
    num2 = int(input("Introduce el segundo número. \n"))

    if num1 < num2:
        parar = True
        for i in range(num1,num2+1):
            if i % 2 != 0:
                print(f"El número {i}")
    else:
        print("El número 1 tiene que ser mayor que el número 2 \n")