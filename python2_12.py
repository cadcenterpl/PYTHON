import sys
from sys import stdin
from sys import stdout
#------------------------------------
lista = list(range(11))
lista0=[]
lista1=[]
lista2=[]
lista3=[]
lista4=[]
lista5=[]
lista6=[]
lista7=[]
lista8=[]
lista9=[]
lista10=[]
i=0
stdout.write("x |")
while (i<10):
    stdout.write("  " + str(lista[i]) + "  ")
    i+=1
stdout.write(" " + str(lista[i])) 
i=0
y=1
stdout.write("\n---------------------------------------------------------\n")
while (i<11):
    if (i<10): stdout.write(str(lista[i]) + " |  ")
    else: stdout.write(str(lista[i]) + "|  ")
    stdout.write(str(lista[i]*0) + "   ")
    while (y<11):
        if int(len(str(lista[i]*y)))<2 : stdout.write(str(lista[i]*y) + "    ")
        else: stdout.write(str(lista[i]*y) + "   ")
        y+=1
    stdout.write("\n")
    y=1
    i+=1
#-----------------------------------
# Kamil Martenczuk 4/26/20
# Troche nakombinowalem ale to moje początki 
