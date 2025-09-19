# Arrays

# Definir array
peliculas = ["Batman", "Spiderman", "Superman", "Avengers", "Ironman"]

# Hay que pasarlo como tupla
cantantes = list(("Ed Sheeran", "Shawn Mendes", "Nil Moliner", "Leiva"))
años = list(range(2025,2051))

print(peliculas)
print(cantantes)
print(años)

#Índices
print(peliculas[1])
print(peliculas[-4])
print(cantantes[1:3])
print(cantantes[:2])
print(cantantes[2:])
print(cantantes[:])

peliculas[peliculas.index("Superman")] = "Star Wars"
print(peliculas)

peliculas.append("Interestellar")
print(peliculas)
peliculas.append("Interestellar")
print(peliculas.count("Interestellar"))
print(peliculas)
peliculas.remove("Interestellar")
print(peliculas)
peliculas.sort()
print(peliculas)

# Recorrer lista

for pelicula in peliculas:
    print(f"La película en posición {peliculas.index(pelicula)+1} es: {pelicula}")

# Listas multidimensionales
contactos = [
    ["Antonio", "antonio@gmail.com", 673452534],
    ["Manuel", "manuel@gmail.com", 642344524],
    ["Iker", "iker@gmail.com", 684532499]
]

print(contactos)
print(contactos[2][1])

for contacto in contactos:
    for info in contacto:
        print(info)
    print()
