import sys
from sys import stdin
from sys import stdout
#------------------------------------
lista = []
stdout.write("Podaj ilosc liczb:  ")
liczba = int(stdin.readline())
i = int(0)
while i<liczba: 
    stdout.write("Podaj liczbe:  ")
    lista.append(int(stdin.readline()))
    i+=1  
stdout.write("Lista liczb: " + str(lista))
#-----------------------------------
# Kamil Martenczuk 4/26/20