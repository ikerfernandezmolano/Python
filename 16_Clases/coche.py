# Programación Orientada a Objetos

class Coche:

    """
    Clase que representa un coche básico.

    Atributos privados: color, marca, plazas, caballaje y velocidad.
    Métodos públicos controlan el acceso y comportamiento.
    """

    """
    Visibilidad de los atributos:
    soy_publico: str
    _soy_protegido: str
    __soy_privado: str
    """

    """
    En Python cuando un atributo de una clase no tiene setter,
    pero si getter, se utiliza @property
    """

    __color: str
    __marca: str
    __plazas: int
    __caballaje: int
    __velocidad: int

    def __init__(self, pColor:str, pMarca:str, pPlazas:int, pCaballaje:int, pVelocidad:int):
        self.__color = pColor
        self.__marca = pMarca
        self.__plazas = pPlazas
        self.__caballaje = pCaballaje
        self.__velocidad = pVelocidad

    def apretarAcelerador(self) -> None:
        self.__acelerar()

    def __acelerar(self) -> None:
        self.__velocidad += 1

    @property
    def velocidad(self) -> int:
        return self.__velocidad