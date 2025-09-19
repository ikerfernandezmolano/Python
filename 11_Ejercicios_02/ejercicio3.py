"""
Ejercicio 3. Programa que compruebe si una variable está vacía
si está vacía, rellenarla con texto en minúsculas y mostrarlo
en mayúsculas.
"""

texto = ""

texto.strip()
if len(texto) == 0 :
    texto = "hola, soy un texto en minúsculas"
    print(texto.upper())
else: 
    print(f"La variable tiene contenido: \n{texto}")