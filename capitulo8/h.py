import sys 
read = sys.stdin.read().split()
n = int(read[0])
m = int(read[1])
k = int(read[2])

adyacencia = [set() for i in range(n+1)]
g = [0] * (n+1)
indice = 3

for i in range(m): 
    u = int(read[indice])
    v = int(read[indice+1])
    adyacencia[u].add(v)
    adyacencia[v].add(u)
    g[u] += 1
    g[v] += 1
    indice+=2

p = True
for j in range(1, n+1): 
    if g[j] % 2 != 0: 
        p = False 
        break 
if not p: 
    print('-1')
else: 
    pila = [k]
    camino = []

    while pila: 
        u = pila[-1]
        if adyacencia[u]: 
            v = adyacencia[u].pop() 
            adyacencia[v].remove(u)
            pila.append(v)
        else: 
            camino.append(pila.pop())
    
    if len(camino) == m+1: 
        print('\n'.join(map(str, camino[::-1])))

    else: 
        print('-1')
