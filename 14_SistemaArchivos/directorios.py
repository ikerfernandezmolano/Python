import os, shutil

# Crear carpeta

if not os.path.isdir(os.path.dirname(os.path.abspath(__file__))+"/carpeta_prueba"):
    os.mkdir(os.path.dirname(os.path.abspath(__file__))+"/carpeta_prueba")
else:
    print("Ya existe el directorio")

# Copiar
ruta_original = os.path.dirname(os.path.abspath(__file__))+"/carpeta_prueba"
ruta_nueva = os.path.dirname(os.path.abspath(__file__))+"/carpeta_prueba_copiada"
shutil.copytree(ruta_original,ruta_nueva)

# Eliminar si el directorio esta vacío
#os.rmdir(os.path.dirname(os.path.abspath(__file__))+"/carpeta_prueba_copiada")

# Eliminar si el directorio tiene elementos
shutil.rmtree(os.path.dirname(os.path.abspath(__file__))+"/carpeta_prueba_copiada")

print("CONTENIDO DE MI CARPETA")
contenido = os.listdir(os.path.dirname(os.path.abspath(__file__))+"/carpeta_prueba")
print(contenido)