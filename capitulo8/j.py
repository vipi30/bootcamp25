import sys 
import heapq 

def dijkstra(comienzo, n, adyacencia):
    dist = [float('inf')] * n 
    dist[comienzo] = 0 
    cola = [(0, comienzo)]

    while cola: 
        actual, u = heapq.heappop(cola)

        if actual > dist[u]: 
            continue 
        for v, peso in adyacencia[u]: 
            if dist[u] + peso < dist[v]: 
                dist[v] = dist[u] + peso 
                heapq.heappush(cola, (dist[v], v))

    return dist 

read = sys.stdin.read().split() 

puntero = 0
n = int(read[puntero])
puntero+=1
m = int(read[puntero])
puntero+=1
d = float(read[puntero])
puntero+=1

indice = []
nombres = {}

for i in range(n): 
    nombre = read[puntero]
    puntero+=1
    indice.append(nombre)
    nombres[nombre] = i 

adyacencia =[[] for i in range(n)]

for j in range(m): 
    un = read[puntero]
    puntero+=1
    vn = read[puntero]
    puntero+=1
    w = float(read[puntero])
    puntero+=1
    u = nombres[un]
    v = nombres[vn]
    adyacencia[u].append((v,w))
    adyacencia[v].append((u,w))

q = int(read[puntero])
puntero+=1

for i in range(q): 
    comienzo1 = nombres[read[puntero]]
    puntero+=1 
    comienzo2 = nombres[read[puntero]]
    puntero+=1

    dist1 = dijkstra(comienzo1, n, adyacencia)
    dist2 = dijkstra(comienzo2, n, adyacencia)

    res = []
    for j in range(n): 
        if dist1[j] != float('inf') and dist2[j] != float('inf'): 
            if abs(dist1[j] - dist2[j]) <= d + 1e-9: 
                res.append(indice[j])
    res.sort()
    print(len(res))
    for k in res: 
        print(k)
