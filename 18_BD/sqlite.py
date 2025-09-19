# Módulo para SQLite
import sqlite3 as sql
import pathlib 

# Conexión
conexion = sql.connect(str(pathlib.Path(__file__).resolve().parent)+"/pruebas.db")

# Crear cursos
cursor = conexion.cursor()

# Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS PRODUCTOS(" +
"TITULO VARCHAR(50) PRIMARY KEY NOT NULL ," +
"DESCRIPCION TEXT," +
"PRECIO DOUBLE" +
")")

# Insertar datos
cursor.execute("INSERT INTO PRODUCTOS VALUES('STARWARS','LA GUERRA DE LAS GALAXIAS',5.5)")

# Lectura datos
cursor.execute("SELECT * FROM PRODUCTOS")
productos = cursor.fetchall()
print(productos)

# Lectura primer dato
cursor.execute("SELECT TITULO FROM PRODUCTOS")
producto = cursor.fetchone()
print(producto[0])

# Insertar muchos registros de golpe
productos1 = [
    ("StarWars I", "LGDLG", 7.5),
    ("StarWars II", "LGDLG", 7.5),
    ("StarWars III", "LGDLG", 7.5),
    ("StarWars IV", "LGDLG", 7.5),
]
cursor.executemany("INSERT INTO PRODUCTOS(TITULO,DESCRIPCION,PRECIO) VALUES(?,?,?)", productos1)

# Lectura datos
cursor.execute("SELECT * FROM PRODUCTOS")
productos = cursor.fetchall()
print(productos)

# Borrar registros
cursor.execute("DELETE FROM PRODUCTOS")

# Guardar cambios
conexion.commit()

# Cerrar conexión
conexion.close()

