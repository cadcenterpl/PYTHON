import sys
from sys import stdin 
from sys import stdout
#------------------------------------
stdout.write("Wpisz dane do zapisu w pliku: ")
dane=stdin.readline()
try:
    with open ("python4_03.txt","w") as plik:
        plik.write(dane)
        plik.close()
        stdout.write("Zapisano\n") 
except PermissionError:
        stdout.write("Brak uprawnien do zapisu!")
try:
    with open ("python4_03.txt","r") as plik:
        stdout.write("Zapisane dane w pliku to: " + plik.read())
        plik.close()
except FileNotFoundError:
        stdout.write("Blad operacji!")
except PermissionError:
        stdout.write("Brak uprawnien do odczytu pliku!")