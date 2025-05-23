#import cb         # esto importa todo el archivo cb.py
from cb import CuentaBancaria  # esto importa solo la clase CuentaBancaria del archivo cb.py
# Crear una instancia de la clase CuentaBancaria
from cc import CuentaCorriente
# from cb import CuentaBancaria

cb1 = CuentaBancaria("Gabriel", "12345678", "1990/01/01")

#print(cb1._nombre_titular)  

"""
print(cb1.mostrar_nombre())
cb1.cambiar_nombre("Gustavo")
print(cb1.mostrar_nombre())
cb1._nombre_titular = "José"
print(cb1._nombre_titular)"""


cc1 = CuentaCorriente("Gabriel", "12345678", "1990/01/01", 1000)
cc2 = CuentaCorriente("Gustavo", "87654321", "1995/05/05", limite_extraccion=1000)

print(cc1._saldo)
print(cc2._saldo)
