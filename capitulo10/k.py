import sys
from bisect import bisect_left 

read = sys.stdin.read().split()
n = int(read[0])
a = list(map(int, read[1:]))
minimo = []

for elemento in a: 
    indice = bisect_left(minimo, elemento)
    if indice < len(minimo): 
        minimo[indice] = elemento
    else: 
        minimo.append(elemento)
print(len(minimo))
