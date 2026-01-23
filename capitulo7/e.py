#subcadena/substring.
#set/conjunto -> una lista que no permite duplicados. 
#len(set)
#set.add()
'''
slicing -> s = "abcdef"; s[1:4] == "bcd".
Para subcadenas de longitud k:
window = s[i : i+k] (de tamaño k si 0 ≤ i ≤ len(s)-k).
'''

import sys

read = iter(sys.stdin.read().split())
s = next(read)
k = int(next(read))

substring = set() 

#Sliding window.
n = len(s)-k+1 #las posiciones que debe revisar. "+1" porque sólo llegaría a la posición anterior, es decir, sólo llega hasta la posición < no <=.

for i in range(n):
    substring.add(s[i:i+k])

print(len(substring)) #la cantidad de conjuntos que hay guardados.
