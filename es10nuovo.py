
nomeInput_txt=str(input("inserisci nome del file "))
nomeInput_txt="C:\\Users\\ETernelli\\Downloads\\"+nomeInput_txt
fileOpen=open(nomeInput_txt,"r")



def sePalindromo(stringa1):
    n=len(stringa1)
    for i in range(0,n-1):
     if stringa1[i]!=stringa1[n-1-i]:
        return 0
    return 1
def quantePalindrome(fileOpen):
    cont=0
    for linea in fileOpen:
        lineaSplit = linea.split()
        for parola in lineaSplit:
            if sePalindromo(parola):
                cont=cont+1
    return cont
print(quantePalindrome(fileOpen))
fileOpen.close()