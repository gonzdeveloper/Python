

def mochila(tamano_mochila, pesos, valores, n):
    
    if n == 0 or tamano_mochila == 0:
        return 0
    
    if pesos[n-1] > tamano_mochila:
        return mochila(tamano_mochila, pesos, valores, n-1)

    # el maximos de los valores con el esapacio disponible que tengo
    return max(valores[n-1] + mochila(tamano_mochila - pesos[n-1], pesos, valores, n-1), 
                mochila(tamano_mochila, pesos, valores, n-1))




if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_mochila = 30
    n = len(valores)

    resultado = mochila(tamano_mochila, pesos, valores, n)
    print(resultado)