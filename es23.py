import os
input_1=input('lato a:')
try:
    a=int(input_1)
except ValueError:
    print('non è intero')
    os._exit()
input_2=input('lato b:')
try:
    b=int(input_2)
except ValueError:
    print('non è intero')
    os._exit()
for riga in range(0,b):
    if riga==0 or riga==(b-1):
        for colona in range(0,a):
            print('\n',end='')
        print('\n',end='')
        else:
            for colonna in range(0,a):
                if colonna==0 or colonna==(a-1):
                    print('',end='')
                else:
                    print('', end='')
                print('\n', end='')