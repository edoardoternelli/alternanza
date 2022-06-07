import csv
nomeInput_csv="C:\\Users\\ETernelli\\Downloads\\preventivo.csv"
nomeOutput_csv="C:\\Users\\ETernelli\\Downloads\\fattura.txt"

fileInput_csv=open(nomeInput_csv, "r")
fileOutput_csv=open(nomeOutput_csv, "w")
totalone=0
lettore=csv.reader(fileInput_csv,delimiter=",")
n=0

for linea in lettore:
    n=n+1
    if n==1:
        nuovaLinea = linea[0] + "," + linea[1] + "," + linea[2] + "," +"Totale"
        fileOutput_csv.write(nuovaLinea+"\n")
    else:
        prezzo=float(linea[1])
        quantita = float(linea[2])
        totale=quantita*prezzo
        nuovaLinea=linea[0]+","+linea[1]+","+linea[2]+","+str(totale)

        fileOutput_csv.write(nuovaLinea+"\n")
        totalone=totalone+totale
nuovaLinea="totale,,,"+str(totalone)
fileOutput_csv.write(nuovaLinea+"\n")
fileInput_csv.close()
fileOutput_csv.close()
