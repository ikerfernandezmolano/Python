from datetime import datetime as date

# Funciones predefinidas
nombre = "Iker Fernández"

# print y type
print(type(nombre))

# el instanceof de Java
if isinstance(nombre, str):
    print("Es un String")
else: 
    print("No es un String")

# Limpiar espacios
frase = "   Hola     "
print(frase)
print(frase.strip())

# Eliminar variables
year = date.now().year
del year

# Longitud de una cadena o lista
print(f"La palabra {nombre} tiene {len(nombre)} caracteres")

# Encontar caracteres
print(nombre.find("á"))

# Reemplazar palabras en un String
print(frase.replace(" ", "@"))

# Mayúsculas y minúsuculas
print(nombre.lower())
print(nombre.upper())