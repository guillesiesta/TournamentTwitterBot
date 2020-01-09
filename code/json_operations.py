import json
import os
import os.path



def cargarJson(url):
    with open(url, 'r') as f:
        array = json.load(f)

    return array

def guardarJson(contenido):
    path = 'jsons/'
    num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
    #print(num_files)
    #antes ponia num_files +1 para ir incrementando el id del json
    #ahora al empezar desde 0 cuando se hace num_files no hace falta sumarle 1
    with open("jsons/dans_test_"+str(num_files)+".json", "w") as f:
        json.dump(contenido, f)
