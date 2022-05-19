while True:
    input_n=input('inserire n ')
    valore=True
    try:
       n=int(input_n)
    except ValueError:
        print(input_n+" non è intero")
        valore=False
        try:
            n = int(input_n)
        except ValueError:
            print(input_n + " non è positivo")
            valore = False
        if valore:
            break
        i=0
        while i<n:
            print('*',end='')
            i=i+1
            print('\n',end='')
            print('finito')

