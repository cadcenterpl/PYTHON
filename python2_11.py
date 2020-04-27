import sys
from sys import stdin
from sys import stdout
#------------------------------------
literki = str("o")
przerwa = str("")
i = int(0)
#------------------------------------
stdout.write("Podaj wysokosc diamentu (3-9) : ")
wys = int(stdin.readline())
while (wys > 9 or wys < 3):
    stdout.write("Podaj wysokosc 3-9 : ")
    wys = int(stdin.readline())
if (wys%2==0):
    i=1
    while i < (wys-1)/2:
        przerwa+=" "
        i+=1 
    i=1
    while i < wys/2+1:
        stdout.write(str(przerwa) + str(literki)+"\n")
        literki+="oo"
        przerwa=przerwa[:-1]
        i+=1 
    i=wys-1
    while i > wys/2-1:
        literki=literki[:-2]
        stdout.write(str(przerwa) + str(literki)+"\n")
        przerwa+=" "
        i-=1 
else:
    i=0
    while i < (wys-1)/2:
        przerwa+=" "
        i+=1 
    i=1
    while i < (wys-1)/2+1:
        stdout.write(str(przerwa) + str(literki)+"\n")
        literki+="oo"
        przerwa=przerwa[:-1]
        i+=1 
    i=wys
    while i > wys/2:
        stdout.write(str(przerwa) + str(literki)+"\n")
        przerwa+=" "
        literki=literki[:-2]
        i-=1 
#-----------------------------------
# Kamil Martenczuk 4/26/20
# Orłem optymalizacji nie jestem :)