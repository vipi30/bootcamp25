import sys
from collections import deque

read = sys.stdin.read().split()
n = int(read[0])
m = int(read[1])

adyacencia = [[] for _ in range(n+1)]
indice = 2

for _ in range(m):
    u = int(read[indice])
    v = int(read[indice+1])
    adyacencia[u].append(v)
    adyacencia[v].append(u)
    indice += 2

vistos = [False] * (n + 1)
valido = []

for i in range(1, n + 1):
    if vistos[i] or not adyacencia[i]:
        if not adyacencia[i]: vistos[i] = True 
        continue
    
    cola = deque([i])
    vistos[i] = True
    
    nodos = 0
    aristas = 0
    
    while cola:
        u = cola.popleft()
        nodos += 1
        
        for v in adyacencia[u]:
            aristas += 1 
            if not vistos[v]:
                vistos[v] = True
                cola.append(v)

    a = aristas // 2
    if nodos >= 2 and a == nodos - 1:
        valido.append(nodos)

valido.sort()
for i in valido:
    print(i)
