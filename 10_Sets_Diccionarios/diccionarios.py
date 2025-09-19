# Algo como un HashMap

tlfns = {
    "Iker" : 684325757,
    "Alubi" : 642938102,
    "Yuri" : 612345678,
    "Ibon" : 698765432
}

print(tlfns)
print(tlfns.get("Yuri"))
tlfns.update({"Otro":623456789})
print(tlfns)
print(tlfns.pop("Otro"))
print(tlfns)
print(tlfns.keys())
print(tlfns.values())

#Diccionarios bidimensionales
contactos = [
    {
        "Nombre" : "Iker",
        "Teléfono": 684325757
    },
    {
        "Nombre" : "Alubi",
        "Teléfono" : 642938102
    },
    {
        "Nombre" : "Yuri",
        "Teléfono" : 612345678
    },
    {
        "Nombre" : "Ibon",
        "Teléfono" : 698765432
    }  
]

for contacto in contactos:
    print(f"Propietario: {contacto["Nombre"]}")
    print(f"Teléfono de contacto: {contacto["Teléfono"]}")
    print()