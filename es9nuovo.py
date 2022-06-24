import itertools

def faiCombinazioni(A):

    temp = permutations(A, 3)
    for i in list(temp):
	print (list(i))


A = [10, 5, 'Hi']
faiCombinazioni(A)