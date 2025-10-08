from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre: str, color: str, edad: int):
        self.nombre = nombre
        self.color = color
        self.edad = edad

    @abstractmethod
    def hacer_sonido(self):
        pass

    @abstractmethod
    def moverse(self):
        pass
    
