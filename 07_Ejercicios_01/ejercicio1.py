from datetime import datetime as date
"""
Ejercicio 1.
    - Crear variables una "país" y otra "continente"
    - Mostrar su valor por pantalla (imprimir)
    - Poner un comentario diciendo el tipo de dato
"""

pais = input("¿De qué país eres? \n")
continente = input("¿De qué continente eres? \n")
año = date.now().year 

print(f"Eres de {pais}, que es de tipo {type(pais)}. Del continente {continente}, que es de tipo {type(continente)}. Estamos en el año {año}, que es de tipo {type(año)}")

