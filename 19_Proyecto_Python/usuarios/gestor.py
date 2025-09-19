from usuarios.usuario import Usuario

class Gestor:
    
    def opciones(self):
        print("""
Acciones disponibles:
    - Login (login)
    - Registro (reg)
""")

    def registro(self):
        print("\nSe ha iniciado la opción de registro...")

        name = input("Introduce tu nombre: ")
        apels = input("Introduce tus apellidos: ")
        email = input("Introduce tu email: ")
        passwd = input("Introduce tu contraseña: ")

        user = Usuario(name,apels,email,passwd)

        print(f"Registro completado con éxito del usuario {name} {apels}, con correo electrónico: {email}")

    def login(self):
        print("\nSe ha iniciado la opción de inicio de sesión...")

        email = input("Introduce tu email: ")
        passwd = input("Introduce tu contraseña: ")