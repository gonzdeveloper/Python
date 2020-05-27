
import random
import math

"""
    Uso de la Media y la Desviación Estandar
    gracias al uso de la Varianza
"""


def media(X):
    return sum(X) / len(X)


def varianza(X):
    mu = media(X)

    acumulador = 0
    for x in X:
        acumulador += (x -mu)**2

    return acumulador / len(X)


def desviacion_estandar(X):
    return math.sqrt(varianza(X))


if __name__ == '__main__':
    X = [random.randint(9,12) for i in range(20)]

    # Calculo de la Media
    mu = media(X)

    # Varianza
    Var = varianza(X)

    #desviación estandar
    sigma = desviacion_estandar(X)


    print(f'Arreglo X: {X}')
    print(f'Media = {mu}')
    print(f'Varianza = {Var}')
    print(f'Desviación Estandar = {sigma}')