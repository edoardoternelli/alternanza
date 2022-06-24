i=0

lista=[]
dim=int(input("acquisisci dimensione "))
for i in range(dim):
    lista.append(int(input("acquisisci elemento " + str(i) + " della lista ")))

def maxMin(lista):
    max = -9999999
    min = 9999999
    for i in range(dim):
        if lista[i]>max:
           max=lista[i]
        if lista[i]<min:
           min=lista[i]
    return [max,min]

m=maxMin(lista)

print("il massimo della lista è " + str(m[0]))
print("il minimo della lista è " + str(m[1]))



