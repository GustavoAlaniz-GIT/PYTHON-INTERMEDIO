
#Solicitar un numero al usuario.
numero = int(input("Ingrese un número: "))

# Determinar si el número es par o impar usando un operador ternario
resultado = "par" if numero % 2 == 0 else "impar"

# Mostrar el resultado
print(f"El número {numero} es {resultado}.")


#OTRA FORMA USANDO UNA EXCEPCION

def es_par_o_impar(numero):
    """
    Determina si un número es par o impar.

    Args:
        numero (int): El número a evaluar.

    Returns:
        str: "par" si el número es par, "impar" si el número es impar.
    """
    return "par" if numero % 2 == 0 else "impar"

# Ejemplo de uso
if __name__ == "__main__":
    try:
        numero = int(input("Ingrese un número: "))
        resultado = es_par_o_impar(numero)
        print(f"El número {numero} es {resultado}.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
        
    