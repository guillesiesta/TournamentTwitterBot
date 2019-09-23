from randomdict import shuffleDict
from random import choice
import time
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



def eliminatorias(lista_jugadores):
    lista_jugadores_eliminados = []

    if(len(lista_jugadores)==1):
        print("El ganador es "+str(list(lista_jugadores)))
        return ""

    if(len(lista_jugadores)==2):
        print("Llega la gran final!")

    for i in range(0,int((len(lista_jugadores))),2):
        iteracion = 0
        local = list(lista_jugadores)[i]
        visitante = list(lista_jugadores)[i+1]
        jugador_eliminado = choice([local,visitante])
        jugador_eliminado = choice([local,visitante])
        jugador_eliminado = choice([local,visitante])
        lista_jugadores_eliminados.append(jugador_eliminado)
        if(jugador_eliminado==local):
            print(visitante+" ha asesinado a "+local+" usando "+lista_jugadores.get(visitante,None))
            #generarJSON
            #capturar imagen de website
            #escribir tuit
        else:
            print(local+" ha asesinado a "+visitante+" usando "+lista_jugadores.get(local,None))
            #generarJSON
            #capturar imagen de website
            #escribir tuit
        time.sleep(2)

    print("Los jugadores "+str(lista_jugadores_eliminados)+" han sido eliminados. Mala suerte. Comienza la siguiente ronda.")
    #eliminar de la lista_jugadores a los jugadores lista_jugadores_eliminados
    for i in lista_jugadores_eliminados:
        lista_jugadores.pop(i)

    print("Los jugadores "+str(list(lista_jugadores))+" pasan a la siguiente ronda. Enhorabuena.")

    return(eliminatorias(lista_jugadores))


#shuffle lista_jugadores
lista_jugadores = shuffleDict(lista_jugadores)

print(list(lista_jugadores))

eliminatorias(lista_jugadores)





#print(choice(list(lista_jugadores.keys())))

#print(lista_jugadores)
