def calcular_promedio(*args):
    """Calcula el promedio de una lista de números."""
    return sum(args) / len(args) if len(args) > 0 else 0

# Solicitar números al usuario
numeros = list(map(float, input("Ingrese una lista de números separados por comas: ").split(",")))

# Calcular el promedio y mostrar el resultado
promedio = calcular_promedio(*numeros)
print(f"El promedio de los números ingresados es: {promedio}")