"""
Ejercicio 2. Escribir un programa que añada
valores a una lista mientras que su longitud
sea menor a 12 y luego mostrarla
"""

def showList(lista):
    if isinstance(lista, list):
        res = str()
        for elem in lista:
            res += f"{elem} "
        print(res)

lista = []

while len(lista) < 12 :
    lista.append(input("Dime un dato: "))

showList(lista)
lista.clear()

for i in range(12):
    lista.append(input("Dime un dato: "))

showList(lista)

