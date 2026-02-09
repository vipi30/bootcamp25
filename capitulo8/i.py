import sys 
import heapq 

def dijkstra(comienzo):
    distancia = {nombre: float('inf') for nombre in l}
    distancia[comienzo] = 0 

    cola = [(0.0, comienzo)]
    
    while cola: 
        d, u = heapq.heappop(cola)
        if d > distancia[u]: 
            continue 

        for v, peso in adyacente[u]: 
            if distancia[u] + peso < distancia[v]: 
                distancia[v] = distancia[u] + peso 
                heapq.heappush(cola, (distancia[v], v))

    return distancia 

read = sys.stdin.read().split()
n = int(read[0])
m = int(read[1])
umbral = float(read[2])

empieza1 = read[3]
empieza2 = read[4]
l = read[5:5+n]

adyacente = {nombre: [] for nombre in l}
puntero = 5+n 

for i in range(m): 
    u = read[puntero]
    v = read[puntero+1]
    w = float(read[puntero+2])

    adyacente[u].append((v, w))
    adyacente[v].append((u, w)) 
    puntero += 3

dist1 = dijkstra(empieza1)
dist2 = dijkstra(empieza2)

puntos = []
m = 1e-9 

for lugar in l: 
    if abs(dist1[lugar] - dist2[lugar]) <= umbral + m: 
        puntos.append(lugar)

puntos.sort() 
print(len(puntos))

for punto in puntos: 
    print(punto)

