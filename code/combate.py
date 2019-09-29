import json

class Combate():
    def __init__(self, combate="combate",local="local", visitante="visitante", fecha="fecha", ganador="ganador",texto="texto"):
        self.local=local
        self.visitante=visitante
        self.fecha=fecha
        self.ganador=ganador
        self.combate=combate
        self.texto=texto

    def printCombate(self):
        c = {"combate":self.combate,"local":self.local,"visitante":self.visitante,"fecha":self.fecha,"ganador":self.ganador,"texto":self.texto}
        return c

    def setGanador(self, ganador):
        self.ganador = ganador

    def setLocal(self,local):
        self.local = local

    def setVisitante(self,visitante):
        self.visitante = visitante

    def setFecha(self,fecha):
        self.fecha = fecha

    def setCombate(self,combate):
        self.combate = combate

    def setTexto(self,texto):
        self.texto = texto

    def getNumeroCombate(self):
        return self.combate

    def getLocal(self):
        return self.local

    def getVisitante(self):
        return self.visitante

    def getGanador(self):
        return self.ganador

    def getFecha(self):
        return self.fecha

    def getTexto(self):
        return self.texto
