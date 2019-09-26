import json

class Combate():
    def __init__(self, combate="combate",local="local", visitante="visitante", fecha="fecha", ganador="ganador"):
        self.local=local
        self.visitante=visitante
        self.fecha=fecha
        self.ganador=ganador
        self.combate=combate

    def printCombate(self):
        c = {"combate":self.combate,"local":self.local,"visitante":self.visitante,"fecha":self.fecha,"ganador":self.ganador}
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
