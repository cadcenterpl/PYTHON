import sys
from sys import stdin
from sys import stdout
#------------------------------------
while True:
    stdout.write("Podaj liczbe:  ")
    x = int(stdin.readline())
    stdout.write("Kwadrat wynosi: " + str(x*x) + "\n")
    stdout.write("Czy policzyć jeszcze raz? (t/n): ")
    dec = str(stdin.readline())
    if dec[0] == 'n' : break 
#-----------------------------------
# Kamil Martenczuk 4/26/20