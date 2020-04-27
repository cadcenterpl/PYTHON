import sys
import math
from sys import stdin
from sys import stdout
from math import sqrt
#------------------------------------
stdout.write("Podaj liczbe: ")
try:
    liczba = int(stdin.readline())
    stdout.write("Pierwiastek tej liczby wynosi: " + str(sqrt(liczba)))
except ValueError:
    stdout.write("Nie pierwiastkujemy ujemnej")
#-----------------------------------
# Kamil Martenczuk 4/26/20