from empleado import Empleado

class Informatico(Empleado):
    __lenguajes: list

    def __init__(self, pLenguajes: list, pNombre: str, pEdad: int, pDNI: str):
        super().__init__(pNombre, pEdad, pDNI)
        self.__lenguajes = pLenguajes

    def knownLanguages(self) -> None:
        res = "Se programar en: "
        for leng in self.__lenguajes:
            res += f"{leng} "
        print(res)

    def sumarHOLA(self) -> int:
        return super()._sumarDNI()+"hola"

    