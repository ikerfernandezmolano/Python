# Funciones
# def nombre_funcion(parametros):
# nombre_funcion(mis_parametros)

# Funciones lambda
# nombre_funcion = lambda parametro: instrucciones

"""
Parámetros

def nombre_funcion(parametro = valor_defecto): (No hay que darle un valor sí o sí)
def nombre_funcion(parametro): (Hay que dar sí o sí un valor)

nombre_funcion(parametro = valor) (No orden)
nombre_funcion(parametro1, parametro2) (En orden)

"""

lista = []

def muestraNombres():
    global lista
    i = 1
    for nombre in lista:
        print(f"Persona {i}: {nombre}")
        i += 1

def muestraNombresEdad(dic):
    i = 1
    for nombre in sorted(dic.keys()):
        print(f"Persona {i}: {nombre}, {dic.get(nombre)} años")
        i += 1

def pedirNombres(num = 5):
    global lista
    for i in range(num):
        lista.append(input("Dame un nombre: "))

def pedirNombresEdad(num):
    dic = {}
    for i in range(num):
        nombre = input("Dame un nombre: ")
        dic.update({nombre : int(input("¿Cuántos años tiene? \n"))})
    return dic
        
def askshownames():
    pedirNombres(int(input("¿Cuántos nombres quieres dar?")))
    muestraNombres()

def askshownamesages():
    muestraNombresEdad(pedirNombresEdad(num = int(input("¿Cuántos nombres quieres dar?"))))

askshownames()
askshownamesages()

printNombre = lambda nombre : print(f"Tu nombre es {nombre}")

printNombre("Iker")
