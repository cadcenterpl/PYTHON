import sys
from sys import stdin 
from sys import stdout
#------------------------------------
stdout.write("Ile liczb podzielnych przez 4 chcesz wyeksportowac do pliku?: ")
a=(int(stdin.readline()))
b=[4*i for i in range (1,a+1)]
try:
    with open ("python4_01.txt","w") as plik:
        plik.write("Wyeksportowane liczby: " + str(b))
        stdout.write("Wyeksportowano")
        plik.close()
except PermissionError:
        stdout.write("Brak uprawnien!")