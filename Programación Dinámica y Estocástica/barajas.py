
"""
    Simulando las probabiliades de las manos
    con naipes de Poker

"""

import random
import collections

PALOS = ['espada', 'corazon', 'rombo','trebol']
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey']


def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))
    
    return barajas


def obtener_mano(barajas, tamano_mano):
    # para obtener un elemento pero no repetido
    mano = random.sample(barajas, tamano_mano)

    return mano


def main(tamano_mano, intentos):
    barajas = crear_baraja()

    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    pares = 0
    trios = 0
    pares_doble = 0
    poker = 0
    full = 0

    for mano in manos:
        valores = []
        posible_full = 0
        posible_pares_doble = 0

        for carta in mano:
            valores.append(carta[1])

        # ocurrencias de los valores
        counter = dict(collections.Counter(valores))

        for val in counter.values():
            if val == 2:
                pares += 1
                posible_full += 1
                posible_pares_doble += 1
            if val == 3:
                trios += 1
                posible_full += 1
            if val == 4:
                poker += 1
        
        if posible_full == 2:
            full += 1
        if posible_pares_doble == 2:
            pares_doble += 1


    probabilidad_par = pares / intenetos
    probabilidad_pares_dobles = pares_doble / intenetos
    probabilidad_trio = trios / intenetos
    probabilidad_poker = poker / intenetos
    probabilidad_full = full / intenetos
    
    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} barajas es de {probabilidad_par}')
    print(f'La probabilidad de obtener un par doble en una mano de {tamano_mano} barajas es de {probabilidad_pares_dobles}')
    print(f'La probabilidad de obtener un trio en una mano de {tamano_mano} barajas es de {probabilidad_trio}')
    print(f'La probabilidad de obtener poker en una mano de {tamano_mano} barajas es de {probabilidad_poker}')
    print(f'La probabilidad de obtener un full en una mano de {tamano_mano} barajas es de {probabilidad_full}')



if __name__ == '__main__':
    tamano_mano = int(input('De cuantas barajas será la mano: '))
    intenetos = int(input('Cuántos intentos para calcular la probabilidad: '))

    # barajas = crear_baraja()
    # mano = obtener_mano(barajas, 5)

    main(tamano_mano, intenetos)

