def check_arguments(*args):
    if len(args) < 3:
        print("Error: No se han pasado suficientes argumentos.")
    else:
        print("Argumentos recibidos:", args)

# Ejemplo de uso
check_arguments(1)  # Esto imprimirá el mensaje de error
check_arguments(1, 2, 5)  # Esto imprimirá los argumentos recibidos