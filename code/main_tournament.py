import json
from tournament import Tournament
from combate import Combate
from ronda import Ronda

def cargarJson(url):
    with open(url, 'r') as f:
        array = json.load(f)

    return array


def main():
    json = cargarJson("dans_test.json")
    nombre=json["torneo"]
    lista_jugadores = json["jugadores"]

    t = Tournament(nombre,lista_jugadores)
    #c = Combates("broncano","visitante","fecha","visitante")

    r = Ronda("1")
    c = Combate()
    c1 = Combate()

    r2 = Ronda("2")

    r.addCombate(c)
    r2.addCombate(c1)

    t.addRonda(r)
    t.addRonda(r2)

    t.printTournament()


if __name__== "__main__":
  main()
