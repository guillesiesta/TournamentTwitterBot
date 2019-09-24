import json

def cargarJson(url):
    with open(url, 'r') as f:
        array = json.load(f)

    return array

def crearEsqueleto(url):
    data = cargarJson(url)
    #return data
    data["BattleRoyale"]={}
    numero_de_jugadores = len(data["jugadores"])
    i=numero_de_jugadores
    ronda=0
    while i>1:
        ronda=ronda+1
        data["BattleRoyale"].update({"ronda_"+str(ronda):{}})
        for x in range (int(i/2)):
            data["BattleRoyale"]["ronda_"+str(ronda)].update({"combate_"+str(x+1):{}})
            data["BattleRoyale"]["ronda_"+str(ronda)]["combate_"+str(x+1)].update({"local":"arma","visitante":"arma","ganador":"","procesado":False })
        with open(url, "w") as f:
            json.dump(data, f)
        i=int(i/2)

    return data

#crearEsqueleto("torneo.json")
