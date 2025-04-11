"""Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
embargo, también intenta crear el archivo si no existe."""

def abrir_o_crear_archivo():
    nombre_archivo = input("Ingrese el nombre del archivo que desea abrir: ")

    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print("Contenido del archivo:")
            print(contenido)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
        print("Creando el archivo...")
        with open(nombre_archivo, 'w') as archivo:
            archivo.write("")  # Crear archivo vacío
        print(f"Archivo '{nombre_archivo}' creado exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Ejecutar la función
abrir_o_crear_archivo()
