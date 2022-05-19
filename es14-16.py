import math
import os

x=input('inerisci numero positivo')
try:
    x=int(x)
except ValueError:
    print('non è intero')
    os._exit(1)
if x>0:
    rad=math.sqrt(x)
    print('la radice è '+str(rad))
else:
    print('non è positivo')