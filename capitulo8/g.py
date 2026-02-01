import sys 
from collections import deque
read = sys.stdin.read().split()

def distancias(inicio, n, grafo): 
    dist = [-1] * (n+1)
    dist[inicio] = 0
    cola = deque([inicio])
    
    while cola: 
        u = cola.popleft() 
        for v, d in grafo[u]:
            if dist[v] == -1: 
                dist[v] = dist[u] + d
                cola.append(v)
    return dist

p = 0
n = int(read[p])
p+=1
t = int(read[p])
p+=1
va = int(read[p])
p+=1
vb = int(read[p])
p+=1

jorge = int(read[p])
p+=1
otro = int(read[p])
p+=1

max_j = va * t 
max_otro = vb * t

adyacencia = [[] for i in range(n+1)]
for i in range(n-1): 
    u = int(read[p])
    p+=1
    v = int(read[p])
    p+=1
    d = int(read[p]) 
    p+=1
    adyacencia[u].append((v,d))
    adyacencia[v].append((u,d))

dist_jorge = distancias(jorge, n, adyacencia)
dist_otro = distancias(otro, n, adyacencia)

p = []

for j in range(1, n+1): 
    if 0 <= dist_jorge[j] <= max_j and 0 <= dist_otro[j] <= max_otro: 
        p.append(j)

print(len(p))
print(*p)




