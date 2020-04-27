import sys
from sys import stdin
from sys import stdout
#------------------------------------
stdout.write("Podaj liczbe A: ")
a = int(stdin.readline())
stdout.write("Podaj liczbe B: ")
b = int(stdin.readline())
stdout.write("Podaj liczbe C: ")
c = int(stdin.readline())
if ((0<a<=10) and (a>b or b>c)): stdout.write("Warunek zostal spelniony")
else: stdout.write("Warunek nie zostal spelniony")
#-----------------------------------
# Kamil Martenczuk 4/26/20