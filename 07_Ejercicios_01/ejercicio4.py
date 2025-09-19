"""
Ejercicio 4. Pedir dos números al usuario y hacer todas las
operaciones básicas de una calculadora
"""

num1 = int(input("Introduce el primer número"))
num2 = int(input("Introduce el segundo número"))

print(f"El resultado de {num1} + {num2} = {num1+num2}")
print(f"El resultado de {num1} - {num2} = {num1-num2}")
print(f"El resultado de {num1} * {num2} = {num1*num2}")
print(f"El resultado de {num1} / {num2} = {num1/num2}")
print(f"El resultado de {num1} % {num2} = {num1%num2}")
print(f"El resultado de {num1} ^ {num2} = {num1**num2}")