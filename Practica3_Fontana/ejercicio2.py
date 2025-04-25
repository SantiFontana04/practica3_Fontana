def buscar_palabra(palabra_buscada, *args):
    print("La palabra fue encontrada." if palabra_buscada in args else "La palabra no está en la lista.")

# Ingreso de datos por teclado
palabras = input("Ingresá palabras separadas por espacio: ").split()
palabra = input("Ingresá la palabra a buscar: ")

buscar_palabra(palabra, *palabras)