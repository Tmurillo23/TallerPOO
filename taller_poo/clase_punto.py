from math import sqrt
class PuntoCartesiano:

    def __init__(self, coordenada_x: float, coordenada_y: float):
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y

    def mostrar(self):
        print(f" Las coordenadas del punto son: ({self.coordenada_x},{self.coordenada_y})")

    def mover(self, coordenada_x_nueva: float, coordenada_y_nueva: float):
        self.coordenada_x = coordenada_x_nueva
        self.coordenada_y = coordenada_y_nueva

    def calcular_distancia(self, coordenada_x1: float,
                           coordenada_y1: float):  # buscar la manera en la que solo se tengan que pasar los puntos
        distancia = sqrt((self.coordenada_x - coordenada_x1) ** 2 - (self.coordenada_y - coordenada_y1) ** 2)
        return distancia


punto_1: PuntoCartesiano = PuntoCartesiano(5, 9)
punto_2 = PuntoCartesiano = PuntoCartesiano(8, 7)
punto_1.mostrar()
print(punto_1.calcular_distancia(punto_2.coordenada_x, punto_2.coordenada_y))
