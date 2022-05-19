import math
while True:
    input_n=input('inserisci numero>0')
try:
n=int(input_n)
except ValueError
print(input_n+"non è un numero intero ")
if n>0
    break;
x=n
c=0
while x>0:
    x=x//10
    c=c+1
acc=n;
i=c
while i>0:
    v=acc//math.pow(10.,i-1);
    print(str(int(v))+'',end='')
    j=0
    while j<v:
        print('*',end='')
        j=j+1
        print('*', end='')
        acc%=int(math.pow(10.,i-1))
        i=i-1

