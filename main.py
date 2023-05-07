from ClaseConjunto import Conjunto
from ManejadorMenu import Menu
def test():
    opc = int(input("desea probar el test 1 = datos correctos 2 = datos incorrectos 0 = salir\n"))
    while opc != 0:
        if opc == 1:
            conjunto1 = Conjunto({1, 2, 3, 4,5,6})
            conjunto2 = Conjunto({3, 6, 9,10})
            conjuntoNuevo = conjunto1 - conjunto2
            print("{} - {}={}".format(conjunto1,conjunto2,conjuntoNuevo))
            conjuntoNuevo = conjunto1 + conjunto2
            print("{} + {}={}".format(conjunto1,conjunto2,conjuntoNuevo))
            print("es el conjuto1 igual al conjunto 2?")
            band = conjunto1 == conjunto2
            if band == False:
                print("los conjuntos no son iguales")
            else:
                print("los conjuntos son iguales")

        if opc == 2:
            conjunto1 = [1,2,3,4]
            conjunto2 = Conjunto({'3', '6', '9', '10'})
            conjuntoNuevo = conjunto1 - conjunto2
            print("{} - {}={}".format(conjunto1, conjunto2, conjuntoNuevo))
            conjuntoNuevo = conjunto1 + conjunto2
            print("{} + {}={}".format(conjunto1, conjunto2, conjuntoNuevo))
            print("es el conjuto1 igual al conjunto 2?")
            band = conjunto1 == conjunto2
            if band == False:
                print("los conjuntos no son iguales")
            else:
                print("los conjuntos son iguales")
        opc = int(input("desea probar el test 1 = datos correctos 2 = datos incorrectos 0 = salir\n"))
if __name__=='__main__':
    opc = input("desea probar los metodos con la funcion test y = si n = no\n")
    if opc == 'y':
        test()
    print("_______main________")
    menu = Menu()
    menu.run()




