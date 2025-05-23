from ca import CuentaAhorro

def main():
    cuenta = CuentaAhorro("Juan Pérez", "12345678", "1990/05/23", saldo=1000)

    print("\n--- Estado inicial ---")
    print(f"Titular: {cuenta._nombre_titular}")
    print(f"DNI: {cuenta._dni_titular}")
    print(f"Saldo inicial: {cuenta.obtener_saldo()}")
    print(f"Edad del titular: {cuenta.obtener_edad()} años")

    print("\n--- Operaciones ---")
    cuenta.depositar(500)
    cuenta.extraer(300)

    print("\n--- Cálculo de interés ---")
    interes = cuenta.calcular_interes()
    print(f"Interés generado: {interes:.2f}")

if __name__ == "__main__":
    main()
