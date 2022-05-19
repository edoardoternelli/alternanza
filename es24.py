while True:
    input_h=input('altezza')
    try:
        h=int(input_h)
    except ValueError:
        pass
    if h>0 or h<=9:
        break;
    c=0
    for riga in range(1,h+1):
      for colonna in range(1,h-riga+1):
                print('',end='')
    c=1
    for j in range(h-riga+1,h+1):
        print(str(c),end='')
        c=c+1
    c=riga-1
    for j in range(h-riga+2,h+1):
        print(str(c),end='')
        c=c-1
        print('\n',end='')