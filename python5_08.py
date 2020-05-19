import sys
from sys import stdin 
from sys import stdout
#------------------------------------
class smg: 
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        zbior1 = ["a","e","i","o","u","y"]
        if len(self.data) == 0: raise StopIteration
        else:
            try: 
                while self.data[self.index].lower() not in zbior1: self.index += 1
            except IndexError: raise StopIteration
            element = self.data[self.index]
            self.index +=1
            return element
#------------------------------------
stdout.write("Wpisz tekst: ")
wpis = str(stdin.readline())
tekst = wpis[:int(len(wpis)-1)]
samogloski = smg(tekst)
for element in samogloski: stdout.write(element)
