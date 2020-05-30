
def run():
    counter = 0
    with open('aleph.txt', encoding='utf8') as archivo:
        for line in archivo:
            counter += line.count('Beatriz')

    print(f'Beatriz se encuentra {counter} veces en el texto')
            


if __name__ == '__main__':
    run()