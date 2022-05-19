import os
input_l=input('inserisci n')
try:
    n=int(input_l)
except ValueError:
    print('non è intero')
    os._exit()
i=0
while i<n:
    print('',end='')
    i=i+1
    print(end='')
    print('*',end='')
