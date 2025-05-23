from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    def __init__(self, nombre):
        self._nombre = nombre #atributo privado
		
    @classmethod
    @abstractmethod
    def calcular_area(self):
        pass
        
    @classmethod
    @abstractmethod
    def calcular_perimetro(self):
        pass

    def obtener_nombre(self):
        return self._nombre