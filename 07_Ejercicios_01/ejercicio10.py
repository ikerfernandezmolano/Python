"""
Ejercicio 10. Pedirá la nota de quince alumnos y sacar cuantos
han aprobado y cuantos han suspendido
"""

alumnos = int(input("¿Cuántos alumnos tienes? \n"))
aprobado = 0

for i in range(alumnos):
    nota = float(input("Introduce una nota: "))
    if nota >= 5.0: 
        aprobado += 1

print(f"Han aprobado {aprobado} alumnos y han suspendido {alumnos-aprobado}")
