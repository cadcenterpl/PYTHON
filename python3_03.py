import sys
from sys import stdin
from sys import stdout
#------------------------------------
produkty={"Szynka":"kilogram", "Szczotka":"sztuka", "Frytki":"kilogram","Baton":"sztuka"}
a=[name for name, value in produkty.items() if value =="sztuka"]
stdout.write(str(a))