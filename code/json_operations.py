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
    with open("jsons/dans_test_"+str(num_files+1)+".json", "w") as f:
        json.dump(contenido, f)
