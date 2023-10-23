from classCrud import Crud
from classProducto import Producto
from classValidacion import Validacion

instanciaValidacion = Validacion("una opción")
instanciaCrud = Crud()


def menu():
    print("""
    1. Añadir producto
    2. Mostrar productos
    3. Modificar producto
    4. Eliminar producto
    5. Salir
    """)
    eleccion = instanciaValidacion.pedirNumeroEntero()
    return eleccion


if __name__ == "__main__":
    while True:
        eleccion = menu()
        if eleccion == 1:
            print(instanciaCrud.añadirProducto())
        elif eleccion == 2:
            instanciaCrud.leerProducto()
        elif eleccion == 3:
            print(instanciaCrud.modificarProducto())
        elif eleccion == 4:
            print(instanciaCrud.eliminarProducto())
        elif eleccion == 5:
            break
        else:
            print('Ingrese una opcion valida.')
