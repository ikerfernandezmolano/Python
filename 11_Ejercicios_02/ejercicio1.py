"""
Ejercicio 1. Obtener una lista con 8 números enteros,
recorrerla y string, ordenarla y mostrarla (función), mostrar su longitud
y buscar un elemento que el usuario pida por teclado.
"""

long = int(input("¿Cuántos números quieres que tenga tu lista? \n"))
lista = []

for i in range(long):
    lista.append(int(input(f"Dime el número {i+1}º : ")))

for elem in lista:
    print(f"{elem}")

def mostrarLista(lista):
    res = str()
    for elem in lista:
        res += f"{elem} "
    return res

print(mostrarLista(lista))

def sortandshow(lista):
    if isinstance(lista,list):
        lista.sort()
    return mostrarLista(lista)

print(sortandshow(lista))

def size(lista):
    if isinstance(lista,list):
        return len(lista)
    return -1

print(size(lista))

def find(lista):
    pos = str()
    dato = -1
    while not isinstance(pos,int) or pos <= 0:
        pos = int(input("Indica la posición del valor que buscas: "))
    if isinstance(lista,list):
        try:
            dato = lista[pos-1]
        except:
            print("La posición indicada no corresponde a una posición en la lista")
            dato = find(lista)
    return dato

print(find(lista))