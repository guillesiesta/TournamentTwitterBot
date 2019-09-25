import json
from combate import Combate

class Ronda():
    def __init__(self,nombre):
        self.ronda=nombre
        self.combates=[] #lista de combates

    def printRonda(self):
        r = {"ronda":self.ronda,"combates":self.getCombates()}
        return r

    def addCombate(self,c):
        self.combates.append(c)

    def getCombates(self):
        lista_combates = []
        for i in self.combates:
            lista_combates.append(i.printCombate())
        return lista_combates
