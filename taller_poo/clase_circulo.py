from math import pi


class PuntoCartesiano:

    def __init__(self, coordenada_x: float, coordenada_y: float):
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y


class Circulo:

    def __init__(self, radio : float, centro : PuntoCartesiano):
        self.radio = radio
        self.centro = centro

    def area(self):
        area = self.radio ** 2 * pi
        return area

    def perimetro(self):
        perimetro = 2 * pi * self.radio
        return perimetro

    def pertenece(self, punto:PuntoCartesiano):
        if (punto.coordenada_x - self.centro.coordenada_x)**2 + (punto.coordenada_y - self.centro.coordenada_y)**2 <= self.radio**2:
            return "El punto pertenece"
        else:
            return "El punto no pertenece"




punto_1: PuntoCartesiano = PuntoCartesiano(5,9)
punto_2: PuntoCartesiano = PuntoCartesiano(15,9)
circunferencia : Circulo = Circulo(5.9, punto_1)
print(circunferencia.pertenece(punto_2))


