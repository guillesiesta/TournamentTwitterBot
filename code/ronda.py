import json
from combate import Combate

class Ronda():
    def __init__(self,nombre):
        self.ronda=nombre
        #self.combates=Combates() #lista de combates
        self.combates=[] #lista de combates

    def printRonda(self):
        r = {"ronda":self.ronda,"combates":[self.getCombates()]}
        return r

    def addRonda(self,index):
        self.ronda={"ronda":str(index)}
        #self.combates.addCombate(c)

    def addCombate(self,c):
        #print(c.printCombate())
        self.combates.append(c)

    def getCombates(self):
        lista_combates = []
        for i in self.combates:
            lista_combates.append(i.printCombate())
        return lista_combates
