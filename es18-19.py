do{

n=print('inserisci valore da 1 a 12')
}while(n<1 || n>12)
do{
giorno=print('inserisci giorno da 1 a 31')
}while(n<1 || n>31)
if n==1
    mese="inverno"
if n==2
    mese="inverno"
if n==3 && giorno==21
    {
    mese="marzo"
    print('equinozio di primavera')
    }

if n==4
    mese="aprile"
if n==5
    mese="maggio"
if n==6 && giorno==21
    {
    mese="giugno"
    print('solstizio d estate')
    }

if n==7
    mese="luglio"
if n==8
    mese="agosto"
if n==9 && giorno==21
    {
    mese = "settembre"
    print('equinozio d autunno')
    }

if n==10
    mese="ottobre"
if n==11
    mese="novembre"
if n==12 && giorno==21
    {
    mese = "dicembre"
    prit('solstizio d inverno')
    }
print(mese)