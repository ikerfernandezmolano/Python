from informatico import Informatico
from empleado import Empleado

emp = Empleado("María", 18, "12345678L")
emp.hablar()

inf = Informatico(["HTML","Java","Python"],
                    "Iker", 20, "234687654T")
inf.hablar()
inf.knownLanguages()
print(inf.sumarDNI())

