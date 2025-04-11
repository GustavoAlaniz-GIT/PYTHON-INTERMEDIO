"""Escribe un programa que intente sumar un número y una cadena. Si se produce un error
de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario."""

def sumar_numero_y_cadena():
    try:
        numero = int(input("Ingrese un número: "))
        cadena = input("Ingrese una cadena de texto: ")
        resultado = numero + cadena  # Esto generará un TypeError
    except TypeError:
        print("Error: No se puede sumar un número y una cadena de texto.")
    except ValueError:
        print("Error: Entrada inválida. Por favor, ingrese un número válido.")
    else:
        print(f"Resultado de la suma: {resultado}")

# Ejecutar la función
sumar_numero_y_cadena()
