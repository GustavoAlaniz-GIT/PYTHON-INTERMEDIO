"""Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario."""

def dividir_dos_numeros():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 / num2
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese números válidos.")
    else:
        print(f"Resultado de la división: {resultado}")
    finally:
        print("Fin del programa.")

# Ejecutar la función
dividir_dos_numeros()
