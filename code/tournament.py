import json
from ronda import Ronda
from json_operations import guardarJson

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
        guardarJson(torneo)

    def getNumeroRondasActual(self):
        return len(self.rondas)

    def getNumeroJugadores(self):
        return len(self.jugadores)

    def getJugadores(self):
        return self.jugadores

    #calculo el numero de rondas totales que habra dependiendo de los jugadores
    def getNumeroDeRondasTotales(self,numero_jugadores):
        rondas=0
        i=numero_jugadores
        while i>1:
            rondas=rondas+1
            i=int(i/2)
        return rondas

    def getNumeroCombatesRondaActual(self):
        l=[]
        for i in self.rondas:
            l.append(i.getCombates())
        return l
