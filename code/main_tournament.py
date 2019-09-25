import json
from tournament import Tournament
from combate import Combate
from ronda import Ronda
from json_operations import cargarJson


def main():
    json = cargarJson("dans_test.json")
    nombre=json["torneo"]
    lista_jugadores = json["jugadores"]

    #creo objeto torneo
    t = Tournament(nombre,lista_jugadores)

    r = Ronda("1")
    c = Combate()
    r.addCombate(c)



    r2 = Ronda("2")
    c1 = Combate()
    c1.setGanador("pollita gay")
    r2.addCombate(c1)
    r2.addCombate(c1)

    t.addRonda(r)
    t.addRonda(r2)

    t.printTournament()
    t.saveTournament()

if __name__== "__main__":
  main()
