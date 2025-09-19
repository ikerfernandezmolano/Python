def helloWorld(name):
    return f"Hello World! How are you {name}"

def find(lista):
    pos = str()
    while not isinstance(pos,int) or pos <= 0:
        pos = int(input("Indica la posición del valor que buscas: "))
    if isinstance(lista,list):
        return lista[pos-1]
    return -1