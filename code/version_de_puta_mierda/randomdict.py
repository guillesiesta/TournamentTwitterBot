import random

def shuffleDict(lista):
    keys = list(lista)
    random.shuffle(keys)
    d2 = {}
    for key in keys: d2[key] = lista[key]

    return d2
