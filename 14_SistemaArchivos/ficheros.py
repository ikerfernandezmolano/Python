from io import open # Abrir archivos
import pathlib # Obtener el path
import shutil # Copiar archivos, renombrar, mover...
import os # Eliminar archivo
import os.path # Comprobar si existe un archivo

# Paths

# Directorio del script actual (Con pathlib y con os.path)
rutaRELATIVA = str(pathlib.Path().absolute()) # El path será el correspondiente a donde se ejecute

rutaPATHLIB = str(pathlib.Path(__file__).resolve().parent) # Coge el path ..
rutaOS_PATH = os.path.dirname(os.path.abspath(__file__)) # __file__ para referirse al fichero actual

if rutaPATHLIB.lower() == rutaOS_PATH.lower():
    print(f"Las rutas son iguales. \n{rutaPATHLIB}")
else:
    print(f"Las rutas no son iguales \n{rutaPATHLIB}\n{rutaOS_PATH}")

# Concatenar
txt_path = os.path.join(rutaOS_PATH, "archivo.txt")
print(f"\n{txt_path}")

#****************************************************

ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"

# Abrir archivo
archivo1 = open(ruta, "a+")

# Escribir
archivo1.write("***TEXTO DE PRUEBA*** \n")

# Cerrar archivo
archivo1.close()

#****************************************************

# Abrir archivo en modo lectura
archivo2 = open(ruta, "r")

# Leer contenido
contenido = archivo2.read()
print(contenido.split("*"))
print(f"\n{contenido}")

# Leer contenido y guardar en lista
lista = archivo2.readlines()
archivo2.close()
print(f"{lista}\n")

#****************************************************

# Copiar
ruta_org = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_texto2.txt"
shutil.copyfile(ruta_org, ruta_nueva)

# Mover
shutil.move(ruta_org,ruta_nueva)

# Eliminar
os.remove(ruta_nueva)

# Comprobar si existe un archivo
print(os.path.abspath(__file__))

if os.path.isfile(str(pathlib.Path(__file__).absolute())):
    print("El archivo existe.")
else:
    print("El archivo no existe.")


