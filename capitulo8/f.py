import sys 
import heapq 

read = sys.stdin.read().split()

indice = 0 
t = int(read[indice])
indice+=1 

for i in range(t): 
    n = int(read[indice])
    m = int(read[indice+1])
    indice += 2
    
    #lista de adyacencia -> contiene parejas (vecino, distancia)
    adyacencia = [[] for i in range(n+1)]
    for j in range(m): 
        u = int(read[indice])
        v = int(read[indice+1])
        w = int(read[indice+2])

        adyacencia[u].append((v,w))
        adyacencia[v].append((u,w))
        indice+=3

    distancia = [float('inf')] * (n+1)
    maneras= [0] * (n+1)
    
    distancia[1] = 0
    maneras[1] = 1 

    cola = [(0,1)]
    while cola:
        actual, u = heapq.heappop(cola)

        if actual > distancia[u]: 
            continue 

        for v, peso in adyacencia[u]: 
            nuevo = actual+peso 

            if nuevo < distancia[v]: #más corto
                distancia[v] = nuevo 
                maneras[v] = maneras[u]
                heapq.heappush(cola, (nuevo, v))

            elif nuevo == distancia[v]: #igual de corto
                maneras[v] += maneras[u]

    if distancia[n] == float('inf'): 
        print(0)

    else: 
        print(maneras[n])
