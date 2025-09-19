# Bucle For
# for variable in elemento_iterables
# break para salir del bucle for

for contador in range(0,6,1):
    print(f"Voy por el número {contador}")
print()

lista = ["¿","Hola","Qué","Tal","?"]

for var in lista:
    print(var)
print()

# Fibonacci
cont = input("¿Cuántos números quieres de la secuencia de fibonacci? \n")
print()
fib1 = 0
fib2 = 1
for i in range(0,int(cont),1):
    print(fib1)
    fibaux = fib1
    fib1 = fib2
    fib2 += fibaux
    