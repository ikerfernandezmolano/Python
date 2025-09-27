# Tkinter
# Módulo para crear interfaces gráficas de usuario

from tkinter import *

# Crear la ventana raíz
ventana = Tk()

# Icono de la ventana
# ventana.iconbitmap("./imagenes/logo.ico") # Funciona en windows
# icono = PhotoImage(file="./imagenes/logo.png")  # usa .png en lugar de .ico
# ventana.iconphoto(True, icono)

# Cambio en el tamaño de la ventana
ventana.geometry("750x450")

# Bloquear el tamaño de la ventana
ventana.resizable(1,1)

# Arrancar y mostrar la ventana hasta que se cierre
ventana.mainloop()
