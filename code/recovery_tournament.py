from randomdict import shuffleDict
from random import choice
from esqueleto_torneo import crearEsqueleto, cargarJson
import time
import json

def recovery_and_continue(url_json):
    torneo_recovery = cargarJson("test.json")
    lista_jugadores = torneo_recovery["jugadores"]

    for i in torneo_recovery.items():
        print(i)

    #print(lista_jugadores)

    return torneo_recovery


recovery_and_continue("test.json")
