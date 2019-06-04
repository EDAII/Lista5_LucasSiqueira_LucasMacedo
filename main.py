from time import time
from decimal import Decimal
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from avl import *
from rbt import *
import numpy as np

TAM_LISTA = 1000
NUM_REPETICOES = 100
INICIO_INTERVALO = 0
FIM_INTERVALO = 20000


def calc_media(results):
    averages = {}

    for key in results.keys():
        averages[key] = sum(results[key]) / len(results[key])
    return averages

def cria_lista_sem_repeticao():
    return random.sample(range(0, TAM_LISTA + 1), TAM_LISTA)

def cria_lista_com_repeticao():
    return [random.randint(INICIO_INTERVALO, FIM_INTERVALO) for x in range(TAM_LISTA)]

def plota_grafico(averages):
    plt.ylabel('Media de Tempo')

    for key in averages.keys():
        plt.bar(key, averages[key])

    plt.show()


if __name__ == "__main__":
    results = {'AVL': [], 'RBT': []}
    result = {'AVL': 0, 'RBT': 0}

    for aux in range(NUM_REPETICOES):
        lista = cria_lista_sem_repeticao()
        # lista_com_repeticao = cria_lista_com_repeticao()

        for key in result.keys():
            if key == 'AVL':
                inicio = time()
                avlTree = AVL_Tree()
                root = None
                for i in lista:
                    root = avlTree.insert(root, i)

            elif key == 'RBT':
                inicio = time()
                rbt = Tree()
                for i in lista:
                    rb_insert(rbt, Node(i))

            fim = time()
            tempo = Decimal(fim - inicio)

            result[key] = tempo
            results[key].append(tempo)

    averages = calc_media(results)


    print('\n\t \t \tMedia de Tempo(Inserções):')
    for key in averages.keys():
        print(key + ': ' + str(averages[key]))

    plota_grafico(averages)
