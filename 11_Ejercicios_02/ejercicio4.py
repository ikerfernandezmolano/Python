"""
Ejercicio 4. Lista con varias clases, imprimir la clase de cada una
"""

lista = []

lista.append("Hola")
lista.append(True)
lista.append(4)
lista.append(list([4,2,5]))

for elem in lista:
    print(f"El tipo de {elem} es : {type(elem)}")