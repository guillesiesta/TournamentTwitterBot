import json

def cargarJson(url):
    with open(url, 'r') as f:
        array = json.load(f)

    return array

def guardarJson(contenido):
    with open("torneo.json", "w") as f:
        json.dump(contenido, f)
