import json
from tournament import Tournament
from combate import Combate
from ronda import Ronda
from json_operations import cargarJson

def cargarTorneo(json):
    nombre=json["torneo"]
    lista_jugadores = json["jugadores"]
    numero_participantes = len(lista_jugadores)
    #creo objeto torneo
    t = Tournament(nombre,numero_participantes,lista_jugadores)

    #compruebo en el json si hay rondas y dentro de ellas si hay combates
    #voy creando los objetos y los voy almacenando en el objeto torneo
    if len(json["rondas"]) != 0:
        for i in json["rondas"]:
            r = Ronda(i.get("ronda"))
            if(len(i.get("combates"))):
                combates = i.get("combates")
                for i in combates:
                    c = Combate(i.get("combate"),i.get("local"),i.get("visitante"),i.get("fecha"),i.get("ganador"))
                    r.addCombate(c)
            t.addRonda(r)
    else:
        t.iniciarTorneo() #crear primera ronda
    #devuelvo el torneo
    return t

def main():
    json = cargarJson("dans_test.json")

    t = cargarTorneo(json)

    '''numero_rondas_actuales = t.getNumeroRondasActual()
    rondas_actuales = t.getRondas()
    numero_jugadores = t.getNumeroJugadores()
    jugadores = t.getJugadores()'''

    #print(t.getNumeroCombatesRondaActual())
    #t.combatir()
    t.printTournament()
    #t.saveTournament()

if __name__== "__main__":
  main()
