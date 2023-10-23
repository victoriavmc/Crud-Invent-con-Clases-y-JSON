import re

class Validacion:
    def __init__(self, texto=''):
        self.__texto = texto

    # GETS: permite obtener el valor del atributo privado
    def getTexto(self):
        return self.__texto

    # SETS: permiten establecer el valor del atributo privado, inicializarlo o cambiarlo
    def setTexto(self, pTexto):
        self.__texto = pTexto

    # Función para pedir un número entero
    def pedirNumeroEntero(self):
        while True:
            try:
                numero = int(input(f'Ingrese {self.getTexto()}: '))
            except ValueError:
                print('Debe ingresar números enteros. \nIntente nuevamente!')
            else:
                if numero >= 1:
                    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
                    return numero
                else:
                    print( 'Debe ingresar números enteros positivos. \nIntente nuevamente!')

    # Función para pedir una cadena de texto sin caracteres especiales
    def pedirStringMayMas(self):
        while True:
            try:
                caracter = input(f'Ingrese {self.getTexto()}: ')
                if not caracter.strip() or any(c in ',<.>/?:;[{]}=+-_)(*&^%$#@!`~¨¡¿?-/`1~|' for c in caracter):
                    raise ValueError
            except ValueError:
                print('Debe ingresar caracteres válidos. \nIntente nuevamente!')
            else:
                return caracter.title()

    # Función para verificar que el número de factura tiene 8 dígitos
    def verNumero(self, pNumero):
        while True:
            if len(str(pNumero)) == 8 and str(pNumero).isdigit():
                return pNumero
            else:
                print(
                    'No cumples con los requisitos. Ingrese un número correspondiente.')
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
                pNumero = self.pedirNumeroEntero()

    # Función para validar la fecha
    def verificarFecha(self):
        while True:
            fecha = input("Ingrese una fecha en el formato DD-MM-23: ")
            patron = r'^\d{2}-\d{2}-23$'
            if re.match(patron, fecha):
                dia, mes, anio = map(int, fecha.split('-'))
                meses_31_dias = [1, 3, 5, 7, 8, 10, 12]
                if mes == 2:
                    if 1 <= dia <= 28:
                        return False
                elif mes in meses_31_dias:
                    if 1 <= dia <= 31:
                        return False
                else:
                    if 1 <= dia <= 30:
                        return False
            print("El formato de fecha es incorrecto o no cumple con las condiciones. Inténtelo nuevamente.")

    #Funcion validar 2 opciones
    def opciones(self):
        while True:
            opc = self.pedirNumeroEntero()
            if opc== 1:
                return True
            elif opc == 2:
                return False
            else:
                print('Intente nuevamente.')