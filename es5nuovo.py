import sys
import numbers

nomeOutput_txt="C:\\Users\\ETernelli\\Downloads\\"+sys.argv[1]


fileOutput=open(nomeOutput_txt,"w")

carattere=''
while carattere!='$':
   carattere=sys.stdin.read(1)
   #print(carattere)
   fileOutput.write(carattere)

fileOutput.close()