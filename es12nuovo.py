nomeInput_txt="C:\\Users\\ETernelli\\Downloads\\testo.txt"
fileOpen=open(nomeInput_txt,"r")

def seAedL(s):

    if ("a" in s) & ("l" in s):
        return  1
    return 0
def quantiAedL(fileOpen):
    cont=0
    for linea in fileOpen:
        lineaSplit = linea.split()
        for parola in lineaSplit:
            if seAedL(str(parola)):
                cont=cont+1
    return cont
print(quantiAedL(fileOpen))
fileOpen.close()