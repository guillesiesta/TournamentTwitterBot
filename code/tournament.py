import json
from ronda import Ronda
from combate import Combate
from json_operations import guardarJson
import random

class Tournament():
    def __init__(self,torneo,participantes,jugadores):
        self.torneo=torneo
        self.participantes=participantes
        self.rondas=[] #lista de rondas
        self.jugadores=jugadores

    def printTournament(self):
        torneo={"torneo":self.torneo,"participantes":self.participantes,"rondas":self.getRondas(),"jugadores":self.jugadores}
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

    def iniciarTorneo(self):
        #si el torneo esta vacio, relleno la primera ronda
        combates_primera_ronda = int(self.participantes/2)
        random.shuffle(self.jugadores)
        lista_jugadores = self.jugadores
        ronda1 = Ronda(1)
        j=0
        for i in range(combates_primera_ronda):
            local = list(lista_jugadores)[j].get("alias")
            visitante = list(lista_jugadores)[j+1].get("alias")
            fecha = "X"
            ganador=""
            c = Combate(i+1,local,visitante,fecha,ganador)
            ronda1.addCombate(c)
            j=j+2

        self.addRonda(ronda1)
        return True

    def combatir(self):
        #primero buscar si hay algun ganador
        '''for i in self.rondas:
            #print(i.getNumeroRonda())
            for j in i.combates:
                #print(j.getNumeroCombate())'''
        return True
