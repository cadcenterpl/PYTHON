import sys
import math
import random
from sys import stdin
from sys import stdout
#------------------------------------
def fun_pit(a,b):
    return math.sqrt(a**2+b**2)
#------------------------------------
a=random.randint(0,100)
b=random.randint(0,100)
stdout.write(str(fun_pit(a,b)))