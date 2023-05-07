class Conjunto(set):
    def __init__(self, *nombreconj, **elemento):
        super().__init__(*nombreconj, **elemento)# define la clase Conjunto que hereda de la clase set de Python y utiliza el método __init__ de la clase set para inicializar un objeto Conjunto con los argumentos que se le pasen

    def getA(self):
        return self.__A

    def getB(self):
        return self.__B

    def __add__(self,otroconjunto):
        return Conjunto(super().__or__(otroconjunto))#super() se utiliza para llamar al método __or__() de la superclase de la clase actual, que es la clase set.

    def __sub__(self, otroconjunto):
        return Conjunto(super().__sub__(otroconjunto))

    def __eq__(self,otroconjunto):
        return isinstance(otroconjunto,Conjunto) and super().__eq__(otroconjunto)#isinstance verifica si el objeto otroconjunto es una instancia de la clase Conjunto. Si es así, se llama al método __eq__ de la clase set para comparar los elementos de ambos conjuntos utilizando el operador ==
