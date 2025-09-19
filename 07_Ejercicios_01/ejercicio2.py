"""
Ejercicio 2. Escribir un script que nos muestre por pantalla 
todos los numeros pares del 1 al 120
"""

txt = str()
for i in range(1,121,2):
    txt += str(i) + " "
print(txt)