"""Escribe un programa que intente acceder a una clave que no existe en un diccionario. 
Si se produce una excepción KeyError, captura la excepción y muestra un mensaje de error al usuario."""

def acceder_a_clave():
    diccionario = {
        "nombre": "Carlos",
        "edad": 30,
        "ciudad": "Madrid"
    }

    try:
        clave = input("Ingrese la clave que desea buscar en el diccionario: ")
        valor = diccionario[clave]
    except KeyError:
        print(f"Error: La clave '{clave}' no existe en el diccionario.")
    else:
        print(f"El valor asociado a la clave '{clave}' es: {valor}")

# Ejecutar la función
acceder_a_clave()
