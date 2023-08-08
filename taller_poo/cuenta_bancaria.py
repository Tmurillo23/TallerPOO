class CuentaBancaria:

    def __init__(self, numero: str, titular: str):  # Este metodo inicializa los objetos de la clase y sus atributos
        self.numero_de_cuenta: str = numero
        self.saldo: float = 0.0
        self.titular: str = titular

    def depositar(self, cantidad: float):
        self.saldo += cantidad

    def retirar(self, cantidad: float) -> float:
        if self.saldo >= cantidad:
            self.saldo -= cantidad
        else:
            cantidad = self.saldo
            self.saldo = 0.0
        return cantidad

    def aplicar_cuota_de_manejo(self):
        self.saldo = (self.saldo) - (self.saldo*0.02)

    def mostrar_detalle(self):


