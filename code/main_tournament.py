import json
from tournament import Tournament
from combates import Combates

def cargarJson(url):
    with open(url, 'r') as f:
        array = json.load(f)

    return array


def main():
    json = cargarJson("dans_test.json")
    nombre=json["torneo"]
    lista_jugadores = json["jugadores"]

    t = Tournament(nombre,lista_jugadores)
    c = Combates("broncano","visitante","fecha","visitante")
    
    t.addRonda("1",c)

    t.printTournament()


if __name__== "__main__":
  main()
