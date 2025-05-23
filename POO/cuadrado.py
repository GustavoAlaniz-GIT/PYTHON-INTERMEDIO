from figura import FiguraGeometrica

class Cuadrado(FiguraGeometrica):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def calcular_area(self, lado):
        return 0
    def calcular_perimetro(self):
        return 1