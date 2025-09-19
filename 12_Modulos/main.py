"""
Modulos: son funcionalidades ya hechas para reutilizar.
(dummy, random, math, etc.)

En python hay muchos módulos. Se pueden consultar aquí:
https://docs.python.org/3/library/math.html#module-math

Podemos conseguir módulos que ya vienen en el lenguaje,
módulos en internet, y también podemos crear los nuestros.
"""

# Importar modulo propio
#import modulo
#from modulo import helloWorld
from modulo import *

print(helloWorld("Iker"))

# Módulo de fechas
from datetime import datetime as d
print(d.now())
fecha = d.now()
fecha_pers = fecha.strftime("%d/%m/%Y, %H:%M:%S")
print(fecha_pers)

print(d.now().timestamp())

# Módulo de matemáticas
import math as m

print(m.sqrt(m.pi))
print(m.log2(512))
print(m.pi)
print(f"Redondear un número a la alta: {m.ceil(m.pi)}")
print(f"Redondear un número a la baja: {m.floor(m.pi)}")

# Módulo random
import random as r
print(f"Número aleatorio entre 0 y 100: {r.randint(0,101)}")