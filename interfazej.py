from abc import ABC, abstractmethod

class Volador(ABC):
    @abstractmethod
    def volar(self):
        pass

class Pajaro(Volador):
    def volar(self):
        return "El pájaro está volando"

class Avion(Volador):
    def volar(self):
        return "El avión despega"

# Uso
objetos = [Pajaro(), Avion()]
for o in objetos:
    print(o.volar())

    