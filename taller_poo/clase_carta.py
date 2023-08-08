class Carta:
    DIAMANTE = "diamante"
    TREBOL = "trebol"
    PICAS = "picas"
    CORAZON = "corazon"

    def __init__(self, valor: str, pinta: str):
        self.valor = valor
        self.pinta = pinta
