from coche import Coche

coche = Coche("Rojo", "Ferrari", 2, 500, 120)
print(coche.getVelocidad())
coche.apretarAcelerador()
print(coche.getVelocidad())

# Detectar tipado

if type(coche) == Coche:
    print("Es un objeto correcto.")
else:
    print("No es de tipo coche")
