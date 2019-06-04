from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from decimal import Decimal
from rbt import Tree, rb_insert, Node, NIL
from avl import AVL_Tree
from time import time
import numpy as np
import random

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

def plota_grafico(averages):
    plt.ylabel('Media de Tempo')

    for key in averages.keys():
        plt.bar(key, averages[key])

    plt.show()

def binary_search(root, key):
    while root != None:
        if root.val == key:
            return
        elif root.val > key:
            root = root.right
        else:
            root = root.left

def binary_search_rbt(root, key):
    while root != NIL:
        if root.key == key:
            return
        elif root.key > key:
            root = root.right
        else:
            root = root.left

if __name__ == "__main__":
    results = {'AVL': [], 'RBT': []}
    result = {'AVL': 0, 'RBT': 0}
    results_search = {'AVL': [], 'RBT': []}
    result_search = {'AVL': 0, 'RBT': 0}

    for aux in range(NUM_REPETICOES):
        lista = cria_lista_sem_repeticao()

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

        for key in result_search.keys():
            if key == 'AVL':
                inicio = time()
                for i in lista:
                    binary_search(root, i)

            elif key == 'RBT':
                inicio = time()
                for i in lista:
                    binary_search_rbt(rbt.root, i)

            fim = time()
            tempo = Decimal(fim - inicio)

            result_search[key] = tempo
            results_search[key].append(tempo)


    averages = calc_media(results)
    averages_search = calc_media(results_search)


    print('\n\t \t \tMedia de Tempo(Inserções):')
    for key in averages.keys():
        print(key + ': ' + str(averages[key]))
    print('\n\t \t \tMedia de Tempo(Busca):')    
    for key in averages.keys():
        print(key + ': ' + str(averages_search[key]))

    plota_grafico(averages)
    plota_grafico(averages_search)
