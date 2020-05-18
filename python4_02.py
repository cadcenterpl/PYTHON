import sys
from sys import stdin 
from sys import stdout
#------------------------------------
try:
    with open ("python4_01.txt","r") as plik:
        a=plik.read()
        stdout.write("Zapisane dane w pliku z poprzedniego zadania to: \n" + str(a))
        plik.close()
except FileNotFoundError:
        stdout.write("Brak pliku!")
except PermissionError:
        stdout.write("Brak uprawnien!")