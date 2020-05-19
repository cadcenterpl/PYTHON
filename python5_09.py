import sys
from sys import stdin 
from sys import stdout
#------------------------------------ 
def smg(data):
    zbior1 = ["a","e","i","o","u","y"]
    zbior2 = ["A","E","I","O","U","Y"]
    if len(data) == 0: raise StopIteration
    else:
        try: 
            for index in range (0, len(data),1):
                if data[index] not in zbior1 and data[index] not in zbior2 : index +=1
                else:
                    element = data[index]
                    yield element
        except IndexError: raise StopIteration
#------------------------------------
stdout.write("Wpisz tekst: ")
wpis = str(stdin.readline())
tekst = wpis[:int(len(wpis)-1)]
gen = smg(tekst)
#------------------------------------
try:
    while True: stdout.write(next(gen) + " Test ")
except StopIteration: StopIteration