class ActividadRealizada:
    def __init__(self, codigoDeBarras=0, nFactura=0, descripcion='', cantidad=0, fecha=''):
        # Constructor de la clase con atributos por defecto
        # Atributo privado para el codigoDeBarras
        self.__codigoDeBarras = codigoDeBarras
        self.__nFactura = nFactura  # Atributo privado para el número de factura
        self.__descripcion = descripcion  # Atributo privado para la descripción
        self.__cantidad = cantidad  # Atributo privado para la cantidad
        self.__fecha = fecha  # Atributo privado para la fecha

    # Getters y Setters de la clase
    def getCodigoDeBarras(self):
        return self.__codigoDeBarras  # Getter para el codigoDeBarras

    def __setIden(self, valor):
        # Setter para el codigoDeBarras debe ser unico y no puede ser modificable.
        self.__codigoDeBarras = valor

    def getNFactura(self):
        return self.__nFactura  # Getter para el número de factura

    def setNFactura(self, nFactura):
        self.__nFactura = nFactura  # Setter para el número de factura

    def getDescripcion(self):
        return self.__descripcion  # Getter para la descripción

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion  # Setter para la descripción

    def getCantidad(self):
        return self.__cantidad  # Getter para la cantidad

    def setCantidad(self, cantidad):
        self.__cantidad = cantidad  # Setter para la cantidad

    def getFecha(self):
        return self.__fecha  # Getter para la fecha

    def setFecha(self, fecha):
        self.__fecha = fecha  # Setter para la fecha

    # Polimorfismo: método para mostrar información
    def mostrar(self):
        # Muestra el codigoDeBarras
        print("Codigo de Barras: ", self.getCodigoDeBarras())
        print("Descripción: ", self.getDescripcion())  # Muestra la descripción