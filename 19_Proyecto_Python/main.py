"""
Proyecto Python y MYSQL:
- Abrir un asistente ->
. Login
    Identifica al usuario y nos preguntará
    . Opciones:
        - Crear nota
        - Mostrar nota
        - Borrar nota
. Registro
    Creará al usuario en la bbdd
"""

import sys
from usuarios.gestor import Gestor

acc = str()
g = Gestor()

while acc!="reg" and acc!="login":
    g.opciones()
    acc = input("¿Qué quieres hacer?: ")
    if acc == "reg":
        g.registro()
    elif acc == "login":
        g.login()
    elif acc == "break":
        sys.exit()
    else:
        print("\nOpción no disponible.")


