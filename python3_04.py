import sys
import math
from sys import stdin
from sys import stdout
#------------------------------------
def monoton(a):
    if (a > 0): stdout.write("Funkcja jest rosnaca.")
    elif (a == 0): stdout.write("Funkcja jest stala.")
    else : stdout.write("Funkcja jest malejaca.")
    return ""

stdout.write("Funkcja Ax2+B+C=0.\n")
stdout.write("Podaj A: ")
a = int(stdin.readline())
stdout.write("Podaj B: ")
b = int(stdin.readline())
stdout.write("Podaj C: ")
c = int(stdin.readline())
stdout.write(str(monoton(a)))

