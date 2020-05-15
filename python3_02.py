import sys
import numpy
from sys import stdin
from sys import stdout
#------------------------------------
m=numpy.random.randint(1,10, size=(4,4))
a = [m[index_x][index_x] for index_x, x in enumerate(m)]
#------------------------------------
stdout.write(str(m)+"\n")
stdout.write(str(a)+"\n")