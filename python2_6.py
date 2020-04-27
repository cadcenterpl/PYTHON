import sys
from sys import stdin
from sys import stdout
#------------------------------------
stdout.write("Podaj zakres liczb podzielnych przez 5 (do): ")
z = stdin.readline()
for x in range (5, int(z)+1, 5): stdout.write(str(x) + " ")
#-----------------------------------
# Kamil Martenczuk 4/26/20