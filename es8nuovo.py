

nomeInput_txt = "C:\\Users\\ETernelli\\Downloads\\testo.txt"
fileOpen=open(nomeInput_txt,"r")

def selection_sort(lista):
    n = len(lista)
    for i in range(n):  # innestiamo il primo  ciclo for
        minimo = lista[i][1]  # il primo valore di minimo coinciderà con l'elemento in posizione i-esima, questo verrà poi confrontato
        trovato = False

        for j in range(i + 1,n):  # ciclo for per trovare il minimo corrente tra i valori successivi all'elemento in posizione i-esima
            if lista[j][1] < minimo:
                trovato = True
                minimo = lista[j][1]
                indice_trovato = j
        if trovato:  # se "trovato" è True significa che abbiamo individuato un nuovo valore di minimo e dobbiamo effettuare uno scambio
            occ = lista[i]
            lista[i] = lista[indice_trovato]
            lista[indice_trovato] = occ

    return lista


lista=[]
for linea in fileOpen:
    lineaSplit=linea.split()
    lista=lista+lineaSplit

print(lista)
#lista = ["ciao","mi","chiamo","edoardo"]
listaLen=[[nome,len(nome)] for nome in lista]


print(listaLen)

l=selection_sort(listaLen)
print(l)
def togliVocali(s):
    nuovaS=""
    vocali=["a","e","i","o","u"]
    for i in range(0,len(s)):
        if s[i] not in vocali:
            nuovaS=nuovaS+s[i]
    return nuovaS
for coppia in l:
    if coppia[1]%2!=0:
        #print(coppia[0])
        print(togliVocali(coppia[0]))


fileOpen.close()
