import sys
from sys import stdin 
from sys import stdout
#------------------------------------
class Wspak: 
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
#------------------------------------
stdout.write("Wpisz tekst: ")
wpis = str(stdin.readline())
tekst = wpis[:int(len(wpis)-1)]
odwrotnie = Wspak(tekst)
for i in range(0,len(tekst)): stdout.write(str(next(odwrotnie)))