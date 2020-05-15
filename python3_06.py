import sys
import math
import random
from sys import stdin
from sys import stdout
#------------------------------------
def fun_okr(a,b,x,y):
    return math.sqrt(((x-a)**2)+((y-b)**2))
#------------------------------------
a= random.randint(0,100)
b= random.randint(0,100)
x=0
y=0
stdout.write(str(fun_okr(a,b,y,x)))