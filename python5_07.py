import sys
from sys import stdin 
from sys import stdout
#------------------------------------
class CoDruga: 
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index = self.index + 2
        return self.data[self.index-1]
#------------------------------------
stdout.write("Wpisz tekst: ")
wpis = str(stdin.readline())
tekst = wpis[:int(len(wpis)-1)]
druga = CoDruga(tekst)
zakres = int(len(tekst)/2)
for i in range(0,zakres): stdout.write(str(next(druga)))