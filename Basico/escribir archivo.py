
def run():
    with open('numeros.txt', 'w') as archivo:
        for i in range(10):
            archivo.write(str(i))
            


if __name__ == '__main__':
    run()