import random

class Nodo: 
    def __init__(self, valor): 
        self.valor = valor 
        self.izquierda = None
        self.derecha = None

def arbol_binario_aleatorio(tamano): 
    if tamano == 0: 
        return None

    tamano_izquierda = random.randint(0, tamano-1) 
    tamano_derecha = tamano - 1 - tamano_izquierda 

    subarbol_izquierdo = arbol_binario_aleatorio(tamano_izquierda) 
    subarbol_derecho = arbol_binario_aleatorio(tamano_derecha) 
 
    raiz = Nodo(random.randint(0, 10)) 
 
    raiz.izquierda = subarbol_izquierdo 
    raiz.derecha = subarbol_derecho 

    return raiz 

def print_arbol(nodo, nivel=0): 
    if nodo is not None: 
        print_arbol(nodo.derecha, nivel + 1) 
        print(" " * 4 * nivel + "->", nodo.valor) 
        print_arbol(nodo.izquierda, nivel + 1) 

arbol = arbol_binario_aleatorio(8) 
print_arbol(arbol)

