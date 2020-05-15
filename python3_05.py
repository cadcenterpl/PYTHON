import sys
import math
from sys import stdin
from sys import stdout
#------------------------------------
def monoton(a1,a2):
    if (a1 == a2): stdout.write("Funkcje sa rownolegle.")
    elif ((a1 * a2) == -1): stdout.write("Funkcje sa prostopadle.")
    else : stdout.write("Funkcje nie sa prostopadle ani rownolegle/")
    return ""
#------------------------------------
stdout.write("Funkcja 1 Ax2+B+C=0.\n")
stdout.write("Podaj A: ")
a1 = int(stdin.readline())
stdout.write("Podaj B: ")
b1 = int(stdin.readline())
stdout.write("Podaj C: ")
c1 = int(stdin.readline())
stdout.write("Funkcja 2 Ax2+B+C=0.\n")
stdout.write("Podaj A: ")
a2 = int(stdin.readline())
stdout.write("Podaj B: ")
b2 = int(stdin.readline())
stdout.write("Podaj C: ")
c2 = int(stdin.readline())
stdout.write(str(monoton(a1,a2)))