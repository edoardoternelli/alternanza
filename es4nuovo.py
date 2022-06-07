import csv
nomeInput_txt="C:\\Users\\ETernelli\\Downloads\\testo.txt"
nomeOutput_txt="C:\\Users\\ETernelli\\Downloads\\nuovoTesto.txt"
lista=[]
fileInput=open(nomeInput_txt,"r")

for linea in fileInput:
    print(linea)
    lista=lista+[linea]
fileInput.close()

fileOutput=open(nomeOutput_txt,"w")
n=len(lista)
print(n)
for i in range(1,n+1):
   print(i)
   nuovaLinea=lista[-i]
   fileOutput.write(nuovaLinea+"\n")
fileOutput.close()