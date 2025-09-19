"""
Ejercicio 5. Crear una lista con el contenido de esta tabla:
Acción  Aventura    Deportes
GTA     Ass Creed   FIFA25
COD     Crash       PRO25
PUBG    PoP         MotoGP25

Mostrar esta información ordenada
"""

videojuegos = [
    {
        "Categoria" : "Acción",
        "Juegos" : ["GTA","COD","PUBG"] 
    },
    {
        "Categoria" : "Aventura",
        "Juegos" : ["Assasins Creed", "Crash Bandicoot", "Prince of Persia"]
    },
    {
        "Categoria" : "Deportes",
        "Juegos" : ["FIFA25", "PRO25", "MotoGP25"]
    }
]

for cat in videojuegos:
    print(f"La categoría {cat["Categoria"]}, tiene como juegos:")
    for juego in cat["Juegos"]:
        print(f"{juego}")