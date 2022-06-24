s="ciao io sono una stringa"
nomeInput_txt="C:\\Users\\ETernelli\\Downloads\\testo.txt"
fileInput=open(nomeInput_txt,"r")
sommaParole=0
sommaCaratteri=0
for linea in fileInput:

    s=linea.split()
    c=len(s)

    sommaParole=sommaParole+c

    for parola in s:
        caratteri=len(parola)
        sommaCaratteri = sommaCaratteri + caratteri
media=sommaCaratteri/sommaParole

print("le parole lette sono: " + str(sommaParole))
print("i caratteri sono: " + str(sommaCaratteri))
print("la lunghezza media delle parole è "+str(media))
fileInput.close()




