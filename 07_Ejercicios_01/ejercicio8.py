"""
Ejercicio 8. Sacar un portentaje de un número dado 
por el usuario
"""

parar = False
while not parar:
    num = int(input("Introduce el número. \n"))
    prcj = float(input(f"¿Qué portentaje quieres sacar de {num}? \n"))

    if prcj <= 100 and prcj >= 0:
        parar = True
        print(f"El resultado es {num*prcj/100}")