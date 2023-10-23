from classProducto import Producto
from classActividadRealizada import ActividadRealizada
from classValidacion import Validacion
from random import randint

import json

listaEntrada = list()
listaSalida = list()

instanciarValidacion = Validacion()


def cargarDatos():
    try:
        with open("productosInventario.json", "r") as archivoJson:
            data = json.load(archivoJson)
            # Crea instancias de la clase Producto a partir de los datos del archivo JSON
            for productoJson in data:
                producto = Producto(
                    productoJson['Codigo de Barras'],
                    productoJson['Descripcion'],
                    productoJson['Existencias'],
                    productoJson['Entrada'],
                    productoJson['Salida'],
                    productoJson['Stock']
                )
    except FileNotFoundError:
        # Si el archivo no existe, se creará una lista vacía.
        pass


cargarDatos()


class Crud():
    def __init__(self, numero1=10000000, numero2=99999999):
        self.__numero1 = numero1
        self.__numero2 = numero2

    # Métodos Get
    def _getNumero1(self):
        return self.__numero1

    def _getNumero2(self):
        return self.__numero2

    # Métodos Set
    def _setNumero1(self, numero1):
        self.__numero1 = numero1

    def _setNumero2(self, numero2):
        self.__numero2 = numero2

    def guardarJson(self):
        data = []
        for producto in Producto.listaProductos:
            data.append({
                'Codigo de Barras': producto.getCodigoDeBarras(),
                'Descripcion': producto.getDescripcion(),
                'Existencias': producto.getExistenciasIniciales(),
                'Entrada': producto.getEntrada(),
                'Salida': producto.getSalida(),
                'Stock': producto.getStock()
            })

        with open("productosInventario.json", "w") as archivoJson:
            json.dump(data, archivoJson, indent=4)

    def __pedirEntrada(self, pCodigoBarras):
        print('COMPRAS REALIZADAS')
        print(f'\n Del codigo {pCodigoBarras}')

        instanciarValidacion.setTexto('número de factura')

        while True:
            nFactura = instanciarValidacion.pedirNumeroEntero()
            nFacturaValido = instanciarValidacion.verNumero(nFactura)
            if nFacturaValido:
                break

        instanciarValidacion.setTexto('la descripcion o nombre del producto')
        descripcion = instanciarValidacion.pedirStringMayMas()

        instanciarValidacion.setTexto('la cantidad del producto adquirido')
        cantidad = instanciarValidacion.pedirNumeroEntero()

        fecha = instanciarValidacion.verificarFecha()

        return nFactura, descripcion, cantidad, fecha

    def __pedirSalida(self, pCodigoBarras, pDescripcion, pStockSinSalida):
        print('\nVENTAS REALIZADAS')
        print(f'\n Del codigo {pCodigoBarras}')
        print(f'Se vendio {pDescripcion}')
        instanciarValidacion.setTexto('número de factura')

        while True:
            nFactura = instanciarValidacion.pedirNumeroEntero()
            nFacturaValido = instanciarValidacion.verNumero(nFactura)
            if nFacturaValido:
                break

        while True:
            instanciarValidacion.setTexto('la cantidad del producto vendido')
            cantidad = instanciarValidacion.pedirNumeroEntero()
            if cantidad > pStockSinSalida:
                print(
                    f'Error en ingresar cantidad del producto en venta. \n Tiene disponible a la venta de 0 a {pStockSinSalida} productos. \n Intente Nuevamente.')
            else:
                break

        fecha = instanciarValidacion.verificarFecha()

        return nFactura, cantidad, fecha

    def añadirProducto(self):
        codNuevo = randint(self._getNumero1(), self._getNumero2())
        # Asegurarse de que el número no se repita
        while codNuevo in Producto.listaProductos:
            codNuevo = randint(self._getNumero1(), self._getNumero2())

        # Numeros de exisatencias sean por defecto
        existenciasIniciales = randint(0, 50)

        # Funcion pedir Entrada

        nFacturaEntrada, descripcion, cantidadEntrada, fechaEntrada = self.__pedirEntrada(
            codNuevo)
        entrada = ActividadRealizada(
            codNuevo, nFacturaEntrada, descripcion, cantidadEntrada, fechaEntrada)
        listaEntrada.append(entrada)

        stockSinSalida = existenciasIniciales + cantidadEntrada
        # Ver si realizo una salida
        cantidadSalida = 0

        validacion = Validacion(
            f'si realizo una venta del producto {descripcion}\n        1. Si 2. No  ')
        opcionHaySalida = validacion.opciones()

        if opcionHaySalida == 1:
            nFacturaSalida, cantidadSalida, fechaSalida = self.__pedirSalida(
                codNuevo, descripcion, stockSinSalida)
            salida = ActividadRealizada(
                codNuevo, nFacturaSalida, descripcion, cantidadSalida, fechaSalida)
            listaSalida.append(salida)

        stock = stockSinSalida - cantidadSalida
        nuevoProducto = Producto(
            codNuevo, descripcion, existenciasIniciales, cantidadEntrada, cantidadSalida, stock)
        self.guardarJson()  # Guarda los datos actualizados en el archivo JSON
        return "Producto añadido con éxito"

    def __buscarProducto(self):
        instanciarValidacion = Validacion('codigo de barra')
        while True:
            codigoProducto = instanciarValidacion.pedirNumeroEntero()
            codigoProductoValido = instanciarValidacion.verNumero(codigoProducto)
            if codigoProductoValido:
                break
        for producto in Producto.listaProductos:
            if codigoProducto == producto.getCodigoDeBarras():
                return producto  
        return None 
    def __actividadesNuevas(self, pDescripcion, pCodigoBarras):
        print(
            f' Del producto {pDescripcion}, con el codigo de barras: {pCodigoBarras}. \n       Ingrese las nuevos datos: ')
        instanciarValidacion = Validacion('número de factura')
        while True:
            nFactura = instanciarValidacion.pedirNumeroEntero()
            nFacturaValido = instanciarValidacion.verNumero(nFactura)
            if nFacturaValido:
                break

        instanciarValidacion.setTexto('la cantidad del producto comprado')
        cantidad = instanciarValidacion.pedirNumeroEntero()

        fecha = instanciarValidacion.verificarFecha()
        return nFactura, cantidad, fecha

    def modificarProducto(self):
        validacion = Validacion(
            'Desea 1. Actualizar datos (compra/venta) 2. Modificar Datos')
        consulta = validacion.opciones()
        producto = self.__buscarProducto()
        if producto:
            codigoBarra = producto.getCodigoDeBarras()
            if consulta:
                print('Ingrese la nueva actividad realizada del producto')
                primerEntrada = producto.getEntrada()
                descripcion = producto.getDescripcion()

                nFacturaEntrada, cantidadEntrada, fechaEntrada = self.__actividadesNuevas(
                    descripcion, codigoBarra)
                cantidadEntrada = cantidadEntrada + primerEntrada

                entradaNueva = ActividadRealizada(
                    codigoBarra, nFacturaEntrada, descripcion, cantidadEntrada, fechaEntrada)
                listaEntrada.append(entradaNueva)

                existenciaInicial = producto.getExistenciasIniciales()
                stockSinSalida = existenciaInicial + cantidadEntrada

                validacion = Validacion(
                    f'si realizo una venta del producto {descripcion}\n        1. Si 2. No  ')
                opcionHaySalida = validacion.opciones()
                if opcionHaySalida == 1:
                    primerSalida = producto.getSalida()
                    nFacturaSalida, cantidadSalida, fechaSalida = self.__pedirSalida(
                        codigoBarra, descripcion, stockSinSalida)
                    cantidadSalida = cantidadSalida + primerSalida
                    salida = ActividadRealizada(
                        codigoBarra, nFacturaSalida, descripcion, cantidadSalida, fechaSalida)
                    listaSalida.append(salida)
                else:
                    cantidadSalida = 0
                producto.setEntrada(cantidadEntrada)
                producto.setSalida(cantidadSalida)
                producto.setStock(stockSinSalida - cantidadSalida)
                self.guardarJson()  # Guarda los datos actualizados en el archivo JSON
                return "Producto actualizado con éxito"
            else:
                print('Ingrese las modificaciones que correspondan del producto')
                nFacturaEntrada, descripcion, cantidadEntrada, fechaEntrada = self.__pedirEntrada(
                    codigoBarra)

                # MODIFICA LA LISTA
                for elemento in listaEntrada:
                    if elemento.getCodigoDeBarras() == codigoBarra:
                        elemento.setNFactura(nFacturaEntrada)
                        elemento.setDescripcion(descripcion)
                        elemento.setCantidad(cantidadEntrada)
                        elemento.setFecha(fechaEntrada)

                existenciaInicial = producto.getExistenciasIniciales()
                stockSinSalida = existenciaInicial + cantidadEntrada

                validacion = Validacion(
                    f'Realiza una modificacion a la venta del producto {descripcion}\n        1. Si 2. No  ')
                opcionHaySalida = validacion.opciones()
                if opcionHaySalida == 1:
                    nFacturaSalida, cantidadSalida, fechaSalida = self.__pedirSalida(
                        codigoBarra, descripcion, stockSinSalida)
                    # MODIFICAR LA LISTA
                    for elemento in listaSalida:
                        if elemento.getCodigoDeBarras() == codigoBarra:
                            elemento.setNFactura(nFacturaEntrada)
                            elemento.setDescripcion(descripcion)
                            elemento.setCantidad(cantidadEntrada)
                            elemento.setFecha(fechaEntrada)
                else:
                    cantidadSalida = 0

                producto.setDescripcion(descripcion)
                producto.setEntrada(cantidadEntrada)
                producto.setSalida(cantidadSalida)
                producto.setStock(stockSinSalida - cantidadSalida)
                self.guardarJson()  # Guarda los datos actualizados en el archivo JSON
                return "Producto modificado con éxito"
        else:
            return "Producto no encontrado"

    def eliminarProducto(self):
        producto = self.__buscarProducto()
        if producto:
            Producto.listaProductos.remove(producto)
            self.guardarJson()  # Guarda los datos actualizados en el archivo JSON
            return "Producto eliminado con éxito"
        return "Producto no encontrado"

    def __consultarProducto(self):
        producto = self.__buscarProducto()
        if producto:
            return producto.mostrar()
        else:
            print("Producto no encontrado")

    def leerProducto(self):
        validacion = Validacion(
            'Desea 1. Buscar cliente en específico. 2. Listar todo.  ')
        opcionLeer = validacion.opciones()

        if opcionLeer:
            self.__consultarProducto()
        else:
            for producto in Producto.listaProductos:
                producto.mostrar()
                print('')
