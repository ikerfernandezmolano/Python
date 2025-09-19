import random as r

cantantes = list(("Ed Sheeran", "Shawn Mendes", "Nil Moliner", "Leiva"))
numeros = list(range(1,9))
r.shuffle(numeros)
print(str(numeros) + "\n")

# Ordenar
numeros.sort()
print(str(numeros) + "\n")

# Añadir elementos
cantantes.insert(2,"Dani Fernández")
print(str(cantantes) + "\n")

# Eliminar elementos
cantantes.pop() # Elimina el ultimo en la fila
cantantes.pop(1) # Elimina por índice
cantantes.remove("Ed Sheeran") # Por nombre
print(str(cantantes) + "\n")

# Invertir
numeros.reverse()
print(str(numeros) + "\n")

# Buscar dentro de una lista
print("Nil Moliner" in cantantes)
print(str("Shawn Mendes" in cantantes) + "\n")

# Contar elementos
print(f"{len(numeros)}\n")

# Conseguir el índice
print(f"{cantantes.index("Dani Fernández")}\n")

# Fusionar listas
cantantes.extend(numeros)
print(f"{cantantes}\n")