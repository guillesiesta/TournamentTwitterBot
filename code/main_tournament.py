from randomdict import shuffleDict
from random import choice
import time
import json
# create list of players
lista_jugadores = {
    "lusesitas":"quesadilla",
    "guille":"alpargata",
    "josete":"mochillo",
    "broncano":"navaja",
    "elias":"cebolla",
    "juanito":"chiste",
    "paco":"pelota",
    "pablo":"aburrimiento"}

torneo = {"BattleRoyale":{}}

def eliminatorias(lista_jugadores,torneo,ronda):
    lista_jugadores_eliminados = []
    if(len(lista_jugadores)==1):
        print("El ganador es "+str(list(lista_jugadores)))
        return ""

    if(len(lista_jugadores)==2):
        print("Llega la gran final!")


    torneo["BattleRoyale"]["ronda"+str(ronda)]= {}
    lucha=0

    for i in range(0,int((len(lista_jugadores))),2):
        local = list(lista_jugadores)[i]
        visitante = list(lista_jugadores)[i+1]
        jugador_eliminado = choice([local,visitante])
        jugador_eliminado = choice([local,visitante])
        jugador_eliminado = choice([local,visitante])
        lista_jugadores_eliminados.append(jugador_eliminado)

        torneo["BattleRoyale"]["ronda"+str(ronda)]["lucha"+str(lucha)]={local:lista_jugadores.get(local,None),visitante:lista_jugadores.get(visitante,None)}
        with open("file.json", "wb") as f:
            f.write(json.dumps(torneo).encode("utf-8"))

        if(jugador_eliminado==local):
            print(visitante+" ha asesinado a "+local+" usando "+lista_jugadores.get(visitante,None))
            torneo["BattleRoyale"]["ronda"+str(ronda)]["lucha"+str(lucha)]={local:lista_jugadores.get(local,None),visitante:lista_jugadores.get(visitante,None), "process":True}
            #generarJSON
            #capturar imagen de website
            #escribir tuit
        else:
            print(local+" ha asesinado a "+visitante+" usando "+lista_jugadores.get(local,None))
            torneo["BattleRoyale"]["ronda"+str(ronda)]["lucha"+str(lucha)]={local:lista_jugadores.get(local,None),visitante:lista_jugadores.get(visitante,None), "process":True}
            #generarJSON
            #capturar imagen de website
            #escribir tuit
        lucha = lucha + 1
        #time.sleep(2)

    print("Los jugadores "+str(lista_jugadores_eliminados)+" han sido eliminados. Mala suerte. Comienza la siguiente ronda.")
    #eliminar de la lista_jugadores a los jugadores lista_jugadores_eliminados
    for i in lista_jugadores_eliminados:
        lista_jugadores.pop(i)

    print("Los jugadores "+str(list(lista_jugadores))+" pasan a la siguiente ronda. Enhorabuena.")

    ronda=ronda+1
    return(eliminatorias(lista_jugadores,torneo,ronda))


#shuffle lista_jugadores
lista_jugadores = shuffleDict(lista_jugadores)

print(list(lista_jugadores))

ronda = 0

eliminatorias(lista_jugadores,torneo,ronda)

#print(choice(list(lista_jugadores.keys())))

#print(lista_jugadores)
