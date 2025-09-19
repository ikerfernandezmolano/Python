#Vacío, null de Java
nada = None
print(f"{nada} que es {type(nada)} \n")

#String
string = "Hola, ¿Qué tal?"
print(f"{string} que es {type(string)} \n")

#Integers
num = 83
print(f"{num} que es {type(num)} \n")

#Decimal/Coma flotante
dec = 9.7
print(f"{dec} que es {type(dec)} \n")

#Boolean
bool1 = True
bool2 = False
print(f"{bool1}, {bool2} que son {type(bool1)}, {type(bool2)} \n")

#Array
list = [1.0, 2, "tres", 4, 'c']
print(f"{list} que es {type(list)}")
for var in list:
    print(f"{var} que es {type(var)}")
print()

#Tupla, que no cambia
tupla = ("hola",2,'c')
print(f"{tupla} que es {type(tupla)} \n")

#Diccionario
dic = {
    "nombre": "Iker",
    "apellido": "Fernández",
    "edad": 20
}
print(f"{dic} que es {type(dic)} \n")

#Rango
rango = range(9)
print(f"{rango} que es {type(range)} \n")

#Byte
byte = b"Probando"
print(f"{byte} que es {type(byte)} \n")

"""
Hacer castings en Python
----------------------------------------------------------------------
"""

num = str(776)
print(f"{num} que es {type(num)} \n")
num = int(776)
print(f"{num} que es {type(num)} \n")
num = float(776)
print(f"{num} que es {type(num)} \n")