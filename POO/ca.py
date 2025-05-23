from cb import CuentaBancaria

class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self.__tasa_interes = 0.001

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Depósito exitoso de {monto}. Nuevo saldo: {self._saldo}")
        else:
            print("El monto debe ser mayor a 0.")

    def extraer(self, monto):
        if monto > 0 and monto <= self._saldo:
            self._saldo -= monto
            print(f"Extracción exitosa de {monto}. Nuevo saldo: {self._saldo}")
        else:
            print("Fondos insuficientes o monto inválido.")

    def calcular_interes(self):
        return self._saldo * self.__tasa_interes