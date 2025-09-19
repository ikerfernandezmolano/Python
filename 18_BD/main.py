import mysql.connector

# Conexion
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="PRUEBA_SQL"
)

# Conexion correcta
# print(database)

cursor = database.cursor(buffered=True)

# Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS PRUEBA_SQL")

# Mostrar bases de datos
cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)

# Crear tablas

cursor.execute("""
CREATE TABLE IF NOT EXISTS VEHICULOS(
ID int(15) AUTO_INCREMENT NOT NULL PRIMARY KEY,
MARCA VARCHAR(40) NOT NULL,
MODELO VARCHAR(40) NOT NULL,
PRECIO FLOAT(10,2) NOT NULL
)
""")

# Mostrar tablas

cursor.execute("SHOW TABLES")

for tab in cursor:
    print(tab)

# Insertar datos

cursor.execute("INSERT INTO VEHICULOS VALUES(null, 'Opel', 'Astra', 18500.20)")

coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Laguna', 15000),
    ('Audi', 'R8', 25000),
    ('Citroen', 'Saxo', 9000)
]

cursor.executemany("INSERT INTO VEHICULOS VALUES(null,%s,%s,%s)",coches)

coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Laguna', 15000),
    ('Audi', 'R8', 25000),
    ('Citroen', 'Saxo', 9000)
]

cursor.executemany("INSERT INTO VEHICULOS VALUES(null,%s,%s,%s)",coches)

# Borrar datos

cursor.execute("SELECT MARCA,MODELO,PRECIO FROM VEHICULOS GROUP BY MARCA,MODELO,PRECIO HAVING COUNT(*)>1")
resu = cursor.fetchall()

for datos in resu:
    cursor.execute("DELETE FROM VEHICULOS WHERE MARCA=%s AND MODELO=%s",(datos[0],datos[1]))
    cursor.execute("INSERT INTO VEHICULOS VALUES(null,%s,%s,%s)",(datos[0],datos[1],datos[2]))

# Actualizar

cursor.execute("UPDATE VEHICULOS SET MODELO='Leon' WHERE MARCA='Seat'")

print(str(cursor.rowcount)+" VEHÍCULOS ACTUALIZADOS!")

database.commit()

# Select

cursor.execute("SELECT DISTINCT MARCA,MODELO FROM VEHICULOS")
res=cursor.fetchall()

for datos in res:
    print(f"En la base de datos tenemos un {datos[0]} {datos[1]}")

