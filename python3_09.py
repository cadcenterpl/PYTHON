import sys
from sys import stdin
from sys import stdout
#------------------------------------
def fun_ciag_il(a1,r,ile):
    iloczyn=a1
    i=1
    while i< ile:
        iloczyn *= a1+i
        i += 1
    return iloczyn
#------------------------------------
a1=int(1)
r=int(1)
ile=int(10)
stdout.write(str(fun_ciag_il(a1,r,ile)))