#grafos no ponderados
#bfs 
import sys 
from collections import deque 

read = sys.stdin.read().split()
n, m, x, y = map(int, read[:4])

a = [[] for _ in range(n+1)]
for i in range(4, len(read), 2): 
    u = int(read[i])
    v = int(read[i+1])
    a[u].append(v)
    a[v].append(u)

cola = deque([x]) #fifo 
#array de padres: cada que descubro un nuevo punto, apunto de cuál vengo. 
padre = [-1] * (n+1)
dist = [-1] * (n+1)

padre[x] = 0
dist[x] = 0

while cola: 
    actual = cola.popleft()
    if actual == y: 
        break #ya hemos llegado
    for vecino in a[actual]: 
        if dist[vecino] == -1: 
            dist[vecino] = dist[actual] +1 
            padre[vecino] = actual 
            cola.append(vecino)
camino = []
p = y
while p != 0: 
    camino.append(p)
    p = padre[p]

print(dist[y])
camino = camino[::-1]
print(*camino)

