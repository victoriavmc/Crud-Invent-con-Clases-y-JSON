from classActividadRealizada import ActividadRealizada

class Producto(ActividadRealizada):
    # Lista para almacenar instancias de productos
    listaProductos = []

    def __init__(self, codigoDeBarras, descripcion, existenciasIniciales, entradas, salidas, stock):
        # Llama al constructor de la clase base con algunos valores por defecto
        super().__init__(codigoDeBarras, 0 , descripcion, 0,'')
        # Atributos específicos de la clase Producto
        self.__existenciasIniciales = existenciasIniciales
        self.__stock = stock
        self.__entrada = entradas  # Añadir atributo de entrada
        self.__salida = salidas  # Añadir atributo de salida
        # Agrega la instancia actual a la lista de productos
        Producto.listaProductos.append(self)

    # Getters y setters para existencias iniciales
    def getExistenciasIniciales(self):
        return self.__existenciasIniciales

    def __setExistenciasIniciales(self, i):
        self.__existenciasIniciales = i

    def getEntrada(self):
        return self.__entrada

    def setEntrada(self, entrada):
        self.__entrada = entrada

    def getSalida(self):
        return self.__salida

    def setSalida(self, salida):
        self.__salida = salida

    # Getters y setters para stock
    def getStock(self):
        return self.__stock

    def setStock(self, stock):
        self.__stock = stock

    # Polimorfismo: método para mostrar información de productos
    def mostrar(self):
        # Llama al método mostrar de la clase base
        super().mostrar()
        print("Existencias Iniciales: ", self.getExistenciasIniciales())
        print('Entradas:', self.getEntrada())
        print('Salidas:', self.getSalida())
        print('Stock:', self.getStock())
