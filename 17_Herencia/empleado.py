class Empleado:
    __nombre: str
    __edad: int
    __dni: str

    def __init__(self, pNombre: str, pEdad: int, pDNI: str):
        self.__nombre = pNombre
        self.__edad = pEdad
        self.__dni = pDNI

    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @property
    def edad(self) -> int:
        return self.__edad

    @property
    def dni(self) -> str:
        return self.__dni
    
    def _sumarHOLA(self) -> int:
        return self.__dni
    
    def hablar(self):
        print(f"Hola, soy {self.__nombre} tengo {self.__edad} años y mi DNI es: {self.__dni}!!")