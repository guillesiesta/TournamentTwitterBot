import json

class Combate():
    def __init__(self):
        self.local="local"
        self.visitante="visitante"
        self.fecha="fecha"
        self.ganador="ganador"

    def printCombate(self):
        c = {"local":self.local,"visitante":self.visitante,"fecha":self.fecha,"ganador":self.ganador}
        return c

    def addCombate(self,c):
        #print(c.printCombate())
        self.combates.append(c.printCombate())
