import sys
from sys import stdin
from sys import stdout
#------------------------------------
i=0
A=[1/x for x in range(1,11)]
B=[2**i for i in range(11)]
C=[x for x in B if x % 4 == 0]
stdout.write(str(A)+"\n")
stdout.write(str(B)+"\n")
stdout.write(str(C)+"\n")