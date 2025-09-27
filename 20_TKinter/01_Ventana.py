# Tkinter
# Módulo para crear interfaces gráficas de usuario

from tkinter import *
import os.path

class Programa:

    def __init__(self):
        self.title = "Interfaz Gráfica"
        self.icon = os.path.abspath("./imagenes/logo.ico")
        self.icon_alt = os.path.abspath("./20_TKinter/imagenes/logo.ico")
        self.size = "750x450"
        self.resizable = False
        # Crear la ventana raíz
        self.ventana = Tk()

    def cargar(self):
        # Mostrar texto en el programa
        self.ventana.title(self.title)
        # Icono de la ventana
        try:
            self.ventana.iconbitmap(self.icon)
            texto = Label(self.ventana, text=self.icon)
        except:
            self.ventana.iconbitmap(self.icon_alt)
            texto = Label(self.ventana, text=self.icon_alt)
        texto.pack()
        # Cambio en el tamaño de la ventana
        self.ventana.geometry(self.size)
        # Bloquear el tamaño de la ventana
        self.ventana.resizable(self.resizable, self.resizable)

    def addText(self, pText):
        texto = Label(self.ventana, text=pText)
        texto.pack()

    def show(self):
        # Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

programa = Programa()
programa.cargar()
programa.addText("Hola Mundo")  
programa.show()
