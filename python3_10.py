import sys
from sys import stdin
from sys import stdout
#------------------------------------
def lista_zakupow(**rzeczy): return len(rzeczy)

produkty={ "cukierki": "kg","jablka": 'kg',"miotla": "sztuki","baton": "sztuki"}
stdout.write(str(lista_zakupow(**produkty)))