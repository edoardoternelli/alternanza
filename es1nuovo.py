import numbers
prodotti={"carote":5,"pere":10,"mele":15}
somma=0
for frutto in prodotti.keys():
    'quantità richieste dai prodotti disponibili '
    prezzo=prodotti.get(frutto)
    quantita=int(input('quanti pezzi di '+frutto+' vuoi '))
    costo=quantita*prezzo
    somma=somma+costo
print("il costo totale è "+str(somma))