def buscar_palabra_en_lista(palabra, *args):
    return "Palabra encontrada" if palabra in args else "Palabra no encontrada"

# Solicitar al usuario ingresar la lista y la palabra a buscar
lista = input("Ingrese palabras separadas por espacios: ").split()
palabra_a_buscar = input("Ingrese la palabra a buscar: ")

# Llamar a la función y mostrar el resultado
resultado = buscar_palabra_en_lista(palabra_a_buscar, *lista)
print(resultado)