# Bucle While
# while condicion:

contador = 0
while contador <= 100:
    print(f"Estoy en el número {contador}")
    contador+=1

contador-=1
nums = ""
while contador >= 0:
    nums += str(contador) + ", "
    contador-=1
print(nums)

num = int(input("¿De qué valor quieres la tabla? \n"))
cont = 1
while cont < 10:
    print(f"{num} x {cont} = {num*cont}")
    cont +=1

# Fibonacci
cont = int(input("¿Cuántos números quieres de la secuencia de fibonacci? \n"))
print()
fib1 = 0
fib2 = 1
while cont != 0:
    print(fib1)
    fibaux = fib1
    fib1 = fib2
    fib2 += fibaux
    cont-=1