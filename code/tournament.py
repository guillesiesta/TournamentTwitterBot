import json
from rondas import Rondas

class Tournament():
    def __init__(self,torneo,jugadores):
        self.torneo=torneo
        self.rondas=Rondas()
        self.jugadores=jugadores

    def printTournament(self):
        torneo={"torneo":self.torneo,"rondas":self.rondas.printRondas(),"jugadores":self.jugadores}
        print(torneo)
        #print(json.dumps(torneo))
        #with open('abc.json', 'w') as outfile:
            #json.dump(data, outfile, indent=4)

    def addRonda(self,indice,c):
        #self.rondas={"ronda":str(indice),"combates":combate}
        self.rondas.addRonda(indice)
        self.rondas.addCombate(c)

    '''def addCombate(self,local,visitante,fecha,ganador):
        self.rondas.addCombate(local,visitante,fecha,ganador)'''
