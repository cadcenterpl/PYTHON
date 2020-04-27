import sys
from sys import stdin
from sys import stdout
#------------------------------------
literki = str("")
stdout.write("Podaj wysokosc wiezy (max 10) : ")
wys = int(stdin.readline())
while (wys > 10 or wys < 1):
    stdout.write("Podaj wysokosc 1-10 : ")
    wys = int(stdin.readline())
i = int(0)
while i < wys:
    literki+="A"
    stdout.write(str(literki)+"\n")
    i+=1 
#-----------------------------------
# Kamil Martenczuk 4/26/20