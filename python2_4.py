import sys
from sys import stdin
from sys import stdout
#------------------------------------
stdout.write("Podaj liczbe: ")
a = int(stdin.readline())
if a<0: a=a*(-1)
stdout.write("Wartosc bezwzgledna tej liczby to: " + str(a))
#-----------------------------------
# Kamil Martenczuk 4/26/20