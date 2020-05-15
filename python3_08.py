import sys
from sys import stdin
from sys import stdout
#------------------------------------
def fun_ciag(a1,r,ile):
    return int(((2*a1 + (ile-1)*r)/2) * ile)
#------------------------------------
a1=int(1)
r=int(1)
ile=int(10)
stdout.write(str(fun_ciag(a1,r,ile)))