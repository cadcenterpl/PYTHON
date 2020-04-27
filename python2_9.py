import sys
from sys import stdin
from sys import stdout
#------------------------------------
suma = int(0)
stdout.write("Podaj liczbe a ja policze sume tworzacych ja cyfr: ")
liczba = str(stdin.readline())
i = int(0)
while i<len(str(liczba))-1: 
    suma+=int(liczba[i])
    i+=1  
stdout.write("Suma cyfr tworzacych podana liczbe to: " + str(suma))
#-----------------------------------
# Kamil Martenczuk 4/26/20
