n=int(input('inserisci n '))
fShort=open("C:\\Users\\ETernelli\\Downloads\\short.txt", "w")
fLong=open("C:\\Users\\ETernelli\\Downloads\\long.txt", "w")
i=0
for i in range(n):
 var=str(input("acquisisci stringa "))

 if len(var)>5:
   fLong.write(var)
   fLong.write("\n")

 else:
   fShort.write(var)
   fShort.write("\n")
fShort.close()
fLong.close()



