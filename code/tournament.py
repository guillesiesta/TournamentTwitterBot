import json
from ronda import Ronda

class Tournament():
    def __init__(self,torneo,jugadores):
        self.torneo=torneo
        self.rondas=[] #lista de rondas
        self.jugadores=jugadores

    def printTournament(self):
        torneo={"torneo":self.torneo,"rondas":self.getRondas(),"jugadores":self.jugadores}
        print(torneo)
        #print(json.dumps(torneo))
        #with open('abc.json', 'w') as outfile:
            #json.dump(data, outfile, indent=4)

    def addRonda(self,lista):
        #self.rondas={"ronda":str(indice),"combates":combate}
        #self.rondas.addRonda(indice)
        self.rondas.append(lista)
        #self.rondas.addCombate(c)

    def getRondas(self):
        lista_rondas=[]
        for i in self.rondas:
            lista_rondas.append(i.printRonda())
        return lista_rondas
