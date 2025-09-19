texto = "Hola, ¿Qué tal?"
texto2 = "Soy Iker."

print(texto)
print(texto2)

#Variables locales y globales
def prueba():
    #global texto
    texto = "Adios"
    print(texto)

prueba()
print(texto)

#Concatenar variables
print(texto + " " + texto2 + "Estoy concatenando dos Strings")

#Hacer un printf
print(f"{texto} {texto2} Estoy utilizando printf")

#Método format
print("{} {} Estoy utilizando el método Format.".format(texto,texto2))