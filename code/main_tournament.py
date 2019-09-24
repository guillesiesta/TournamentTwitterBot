from randomdict import shuffleDict
from random import choice
from esqueleto_torneo import crearEsqueleto
import time
import json

def eliminatorias(lista_jugadores,torneo,ronda):

    #lista donde guardaré los jugadores que se van a eliminar
    lista_jugadores_eliminados = []

    if(len(lista_jugadores)==1):
        print("FINAL-------------------------------------------------------------------------------------------")
        print("El ganador es "+str(list(lista_jugadores)))
        return ""

    print("RONDA_"+str(ronda)+"---------------------------------------------------------------------------------")
    #extraigo las rondas totales
    rondas_totales = len(torneo["BattleRoyale"])

    if(len(lista_jugadores)==2):
        print("Llega la gran final!")

    lucha=1
    for i in range(0,int((len(lista_jugadores))),2):
        local = list(lista_jugadores)[i]
        visitante = list(lista_jugadores)[i+1]
        jugador_eliminado = choice([local,visitante])
        jugador_eliminado = choice([local,visitante])
        jugador_eliminado = choice([local,visitante])
        lista_jugadores_eliminados.append(jugador_eliminado)

        if(torneo["BattleRoyale"]["ronda_"+str(ronda)]["combate_"+str(lucha)].get("procesado") == False):
            torneo["BattleRoyale"]["ronda_"+str(ronda)]["combate_"+str(lucha)][local] = torneo["BattleRoyale"]["ronda_"+str(ronda)]["combate_"+str(lucha)]["local"]
            del torneo["BattleRoyale"]["ronda_"+str(ronda)]["combate_"+str(lucha)]["local"]

            torneo["BattleRoyale"]["ronda_"+str(ronda)]["combate_"+str(lucha)][local]= (lista_jugadores.get(local,None))

            torneo["BattleRoyale"]["ronda_"+str(ronda)]["combate_"+str(lucha)][visitante] = torneo["BattleRoyale"]["ronda_"+str(ronda)]["combate_"+str(lucha)]["visitante"]
            del torneo["BattleRoyale"]["ronda_"+str(ronda)]["combate_"+str(lucha)]["visitante"]
            
            torneo["BattleRoyale"]["ronda_"+str(ronda)]["combate_"+str(lucha)][visitante]=(lista_jugadores.get(visitante,None))
            
            if(jugador_eliminado==local):
                print(visitante+" ha asesinado a "+local+" usando "+lista_jugadores.get(visitante,None))
                ganador=visitante
                #generarJSON
                #capturar imagen de website
                #escribir tuit
            else:
                print(local+" ha asesinado a "+visitante+" usando "+lista_jugadores.get(local,None))
                ganador=local
                #generarJSON
                #capturar imagen de website
                #escribir tuit
            torneo["BattleRoyale"]["ronda_"+str(ronda)]["combate_"+str(lucha)]["ganador"] = ganador
            torneo["BattleRoyale"]["ronda_"+str(ronda)]["combate_"+str(lucha)]["procesado"] = True
            with open("file.json", "w") as f:
                #f.write(json.dumps(torneo).encode("utf-8"))
                json.dump(torneo, f)

            lucha = lucha + 1
            #time.sleep(2)

    print("Los jugadores "+str(lista_jugadores_eliminados)+" han sido eliminados. Mala suerte. Comienza la siguiente ronda.")
    #eliminar de la lista_jugadores a los jugadores lista_jugadores_eliminados
    for i in lista_jugadores_eliminados:
        lista_jugadores.pop(i)

    print("Los jugadores "+str(list(lista_jugadores))+" pasan a la siguiente ronda. Enhorabuena.")

    ronda=ronda+1
    return(eliminatorias(lista_jugadores,torneo,ronda))

#cargo esqueleto/modelo de torneo con jugadores ya metidos en el json
torneo = crearEsqueleto("file.json")

#extraigo la lista de jugadores
lista_jugadores = torneo["jugadores"]

#shuffle lista_jugadores
lista_jugadores = shuffleDict(lista_jugadores)

#rondas = len(torneo["BattleRoyale"])
#print(rondas)

ronda=1
#lanzo el proceso recursivo de eliminatoria
eliminatorias(lista_jugadores,torneo,ronda)

'''if(torneo["BattleRoyale"]["ronda_1"]["combate_1"].get("procesado") == False):
    print(type(torneo["BattleRoyale"]["ronda_1"]["combate_1"].get("procesado")))'''
