import json
from combates import Combates

class Rondas():
    def __init__(self):
        self.ronda=""
        self.combates=Combates("","","","")

    def printRondas(self):
        r = {"ronda":self.ronda,"combates":[self.combates.printCombate()]}
        return r

    def addRonda(self,index):
        self.ronda={"ronda":str(index),"combates":[self.combates.printCombate()]}

    def addCombate(self,c):
        #print(c.printCombate())
        self.combates.addCombate(c)
