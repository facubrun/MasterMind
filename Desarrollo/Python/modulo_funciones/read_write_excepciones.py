
SALIDA = "SALIR"
LISTA = "LISTA"
ARCHIVO_LISTA = "lista_compra.txt"

lista_mercado = ["papas", "fideos", "galletas"]

def preguntar_usuario_producto():
    return input("Introduzca un producto a su lista: [{} para salir/{} para ver la lista]: ".format(SALIDA,LISTA))

def guardar_lista(lista_compra):
    with open(ARCHIVO_LISTA,"w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))

def cargar_o_crear_lista():
    lista_compra = []
    try:
        if input("Quieres cargar la última lista de la compra? [S/N]: ") == "S":
            with open(ARCHIVO_LISTA, "r") as a:
                lista_compra = a.read().split("\n")
    except FileNotFoundError:
        print("Archivo no encontrado!")
    return lista_compra

def mostrar_lista(lista):
    print("\n".join(lista))

def guardar_producto(lista_compra, producto_a_guardar):
    if producto_a_guardar.lower() in [a.lower() for a in lista_compra]:
        print("El producto ya está en su lista!")
    elif producto_a_guardar.lower() in [a.lower() for a in lista_mercado]:
        print("El producto fue agregado.")
        lista_compra.append(producto_a_guardar)
    elif producto_a_guardar == LISTA:
        print("\n".join(lista_mercado))

def main():
    lista_compra = cargar_o_crear_lista()
    mostrar_lista(lista_compra)

    eleccion_usuario = preguntar_usuario_producto()
    while eleccion_usuario != SALIDA:
        guardar_producto(lista_compra,eleccion_usuario)
        eleccion_usuario = preguntar_usuario_producto()
    mostrar_lista(lista_compra)
    guardar_lista(lista_compra)


if __name__ == "__main__":
    main()