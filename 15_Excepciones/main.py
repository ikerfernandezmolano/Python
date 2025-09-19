# Capturar excepciones y manejar errores en código
# susceptible a fallos/errores

try:
    nombre = input("¿Cuál es tu nombre? :")
    print(nombre)

    if len(nombre)>1:
        nombre_usuario = "El nombre es" + nombre
    print(nombre_usuario)
except:
    print("Ha ocurrido un error, mete bien el nombre")
else:
    print("Esto entra cuando termina el try sin ningún error.")
finally:
    print("Esto lo hace siempre, se genere o no error")

# Múltiples excepciones
try:
    numero = input("Número para elevarla al cuadrado: ")
    print("El cuadrado es: " + str(numero**2))
except TypeError:
    print("Debes convertir el número a entero.")
except ValueError:
    print("Introduce un número correcto")
except Exception as e:
    print(f"Ha ocurrido un error: {type(e).__name__}")

# Excepciones personalizadas o lanzar excepcion

def datos():
    try:
        nombre = input("Introduce el nombre: ")
        edad = int(input("Introduce la edad: "))

        if edad < 5 or edad > 110:
            raise ValueError("La edad introducida no es real")
        elif len(nombre) <= 1:
            raise ValueError("El nombre no es correcto")
        else:
            print(f"Datos introducidos correctamente {nombre}")
    except ValueError:
        print("Introduce los datos correctamente")
        datos()
    except Exception as e:
        print(f"Ha saltado un error de tipo: {type(e).__name__}")
