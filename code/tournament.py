import json
from ronda import Ronda

class Tournament():
    def __init__(self,torneo,jugadores):
        self.torneo=torneo
        self.rondas=[] #lista de rondas
        self.jugadores=jugadores

    def printTournament(self):
        torneo={"torneo":self.torneo,"rondas":self.getRondas(),"jugadores":self.jugadores}
        print(json.dumps(torneo))
        return(torneo)

    def addRonda(self,lista):
        self.rondas.append(lista)

    def getRondas(self):
        lista_rondas=[]
        for i in self.rondas:
            lista_rondas.append(i.printRonda())
        return lista_rondas

    def saveTournament(self):
        torneo = self.printTournament()
        with open("torneo.json", "w") as f:
            json.dump(torneo, f)
