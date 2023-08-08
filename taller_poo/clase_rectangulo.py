class PuntoCartesiano:

    def __init__(self, coordenada_x: float, coordenada_y: float):
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y


class Rectangulo:

    def __init__(self, punto_1: PuntoCartesiano, punto_2: PuntoCartesiano):
        self.punto_1 = punto_1
        self.punto_2 = punto_2

    def area(self):
        base = self.punto_2.coordenada_x - self.punto_1.coordenada_x
        altura = self.punto_2.coordenada_y - self.punto_1.coordenada_y
        return print(base * altura)

    def perimetro(self):
        base = self.punto_2.coordenada_x - self.punto_1.coordenada_x
        altura = self.punto_2.coordenada_y - self.punto_1.coordenada_y
        return (base * 2) + (altura * 2)

    def cuadrado(self):
        base = self.punto_2.coordenada_x - self.punto_1.coordenada_x
        altura = self.punto_2.coordenada_y - self.punto_1.coordenada_y
        if base == altura:
            return "Este rectangulo es un cuadrado"
        else:
            return "Este rectangulo no es un cuadrado"

punto_1: PuntoCartesiano = PuntoCartesiano(5,9)
punto_2: PuntoCartesiano = PuntoCartesiano(15,9)
rectangulo : Rectangulo = Rectangulo(punto_1,punto_2)

print(rectangulo.cuadrado())
