import sys
import math
from sys import stdin
from sys import stdout
from math import sqrt
#------------------------------------
stdout.write("Podaj liczbe: ")
try:
    liczba = int(stdin.readline())
    stdout.write("Ok. Podano liczbe")
except ValueError:
    stdout.write("Wpisujemy tylko cyfry")
#-----------------------------------
# Kamil Martenczuk 4/26/20