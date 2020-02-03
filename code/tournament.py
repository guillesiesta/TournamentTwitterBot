import json
from ronda import Ronda
from combate import Combate
from json_operations import guardarJson
import random
from random import choice

class Tournament():
    def __init__(self,torneo,participantes,jugadores):
        self.torneo=torneo
        self.participantes=participantes
        self.rondas=[] #lista de rondas
        self.jugadores=jugadores

    def printTournament(self):
        torneo={"torneo":self.torneo,"participantes":self.participantes,"rondas":self.getRondas(),"jugadores":self.jugadores}
        #print(json.dumps(torneo))
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
    def getNumeroDeRondasTotales(self):
        rondas=0
        i=self.participantes
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
            fecha = ""
            ganador=""
            texto=""
            c = Combate(i+1,local,visitante,fecha,ganador,texto)
            ronda1.addCombate(c)
            j=j+2

        self.addRonda(ronda1)
        self.saveTournament()
        return True

    def combatir(self,ronda):
        ganadores = []
        combates = ronda.getObjectCombates()

        for j in combates:
            if(j.getGanador()==""):
                local = j.getLocal()
                visitante = j.getVisitante()
                jugador_ganador = choice([local,visitante])
                j.setGanador(jugador_ganador)
                texto_tuit = self.escribirTextoTuit(local,visitante,jugador_ganador)
                j.setTexto(texto_tuit)
                ganadores.append(jugador_ganador)
                self.saveTournament()
                print(texto_tuit)

        if(len(ganadores)==1):
            return True

        ronda = self.generarRondaConGanadores(ganadores,ronda.getNumeroRonda()+1)

        self.combatir(ronda)

    def generarRondaConGanadores(self,ganadores,n_ronda):
        lista_jugadores = ganadores
        combates_por_ronda = int(len(ganadores)/2)
        ronda = Ronda(n_ronda)
        j=0
        for i in range(combates_por_ronda):
            local = list(lista_jugadores)[j]
            visitante = list(lista_jugadores)[j+1]
            fecha = ""
            ganador=""
            c = Combate(i+1,local,visitante,fecha,ganador)
            ronda.addCombate(c)
            j=j+2
        self.addRonda(ronda)
        self.saveTournament()
        return ronda


    def escribirTextoTuit(self,local,visitante,jugador_ganador):
        local = local
        visitante = visitante
        jugador_ganador = jugador_ganador

        #random para expresion para decir de distintas formas que uno mata a otro
        expresion = choice([" se ha cepillado a ", " mata a ", " ha finalizado la vida de ", " le ha dado una paliza a ", " ha asesinado a ", " ha ejecutado a "])
        #genero la frase del tuit
        if(jugador_ganador==local):
            texto_tuit = local + expresion + visitante + " con su "+self.findWeaponByName(local)
        elif(jugador_ganador==visitante):
            texto_tuit = visitante + expresion + local + " con su "+self.findWeaponByName(visitante)

        return texto_tuit

    def findWeaponByName(self,name):
        weapon = ""
        for x in list(self.getJugadores()):
            if x.get("alias") == name:
                weapon = x.get("arma")
                break
        return weapon
