nomeInput_txt="C:\\Users\\ETernelli\\Downloads\\testo.txt"
fileOpen=open(nomeInput_txt,"r")

def sePrimo(num):

    for i in range(2,num-1):
     if num%i==0:
        return 0
    return 1
def quantiPrimi(fileOpen):
    cont=0
    for linea in fileOpen:
        lineaSplit = linea.split()
        for parola in lineaSplit:
            if sePrimo(int(parola)):
                cont=cont+1
    return cont
print(quantiPrimi(fileOpen))
fileOpen.close()