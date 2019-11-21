#!/usr/bin/env python3
"""
Proyecto Polinomio de Lagrange.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

def polinomio_lagrange(X, Y):
    """
    Implementa y retorna el Polinomio de Lagrange para las listas X e Y.

    Parámetros:
    X: lista de valores de la variable independiente.
    Y: lista de valores de la variable dependiente.
    """ 

    if len(X) != len(Y): raise ValueError("Dimensiones diferentes en X e Y.")

    # Ordena el par (x, y) en forma ascendente por x.
    pares = list(zip(X, Y))
    pares.sort(key = lambda x: x[0])
    X, Y  = zip(*pares)

    def polinomio(x):
        lon = len(X)
        px = 0
        a = 0
        while(a < lon):
            l = Y[a]
            b = 0
            while(b < lon):
                if b != a:
                    l = l * ((x - X[b]) / (X[a] - X[b]))
                b += 1 
            px += l
            a += 1
        return px
    return polinomio


if __name__ == '__main__':
    # Pruebe aquí su Polinomio de Lagrange ...
    x=[-2,0,2,4]
    y=[1,-1,3,-2]
    p=polinomio_lagrange(x, y)
    print(p(4))
    pass