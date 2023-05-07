from ClaseConjunto import Conjunto
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1: self.opcion1,
                            2: self.opcion2,
                            3:self.opcion3,


                        }
    def run(self):
        band = True
        while band == True:
            b = int(input("""
    Menu Principal:
1- para sumar dos conjuntos sobrecargando +
2- para restar dos conjuntos sobrecargando -
3- para saber si dos conjuntos son iguales sobrecargando ==
0-salir\n"""))
            func = self.__switcher.get(b)
            if func:
                func()
            else:
                band = False

    def opcion1(self):
        conjuntoA = Conjunto({1, 2, 3, 4})
        conjuntoB = Conjunto({3, 6, 9})
        conjuntonuevo = conjuntoA + conjuntoB
        print(conjuntonuevo)

    def opcion2(self):
        conjuntoA = Conjunto({1, 2, 3, 4})
        conjuntoB = Conjunto({3, 6, 9})
        conjuntonuevo = conjuntoA - conjuntoB
        print(conjuntonuevo)

    def opcion3(self):
        conjuntoA = Conjunto({1, 2, 3, 4})
        conjuntoB = Conjunto({3, 6, 9})
        band = conjuntoA == conjuntoB
        if band == False:
            print("los conjuntos no son iguales")
        else:
            print("los conjuntos son iguales")





