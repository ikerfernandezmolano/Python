from datetime import datetime as date

"""
*Operadores de comparación*

== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

*Operadores lógicos*

and (añadir)
or (o lógico)
not (negar)

"""

# Condicionales
nombre = input("¿Cuál es tu nombre? \n")
nombre = nombre.lower()

if nombre=="iker":
    print("Acceso autorizado.")
elif nombre=="william":
    print("Enseña tu acreditación al personal para pasar.")
else:
    print("Acceso denegado.")

year = input("¿En qué año estamos? \n")

if int(year) != date.now().year:
    print(f"Te has equivocado! Estamos en {date.now().year}")
else:
    print("Correcto!")

edad = input("¿Cuántos años tienes? \n")

if int(edad) >= 16:
    nacionalidad = input("¿En qué país vives? \n")

    if nacionalidad == "España" and int(edad) >= 18:
        print("Eres mayor de edad!")
    else:
        print("No puedo comprobar si en tu país estás considerado como mayor de edad.")

else:
    print(f"No eres mayor de edad, tienes {edad} años.")