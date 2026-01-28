import sys
import heapq 

read = iter(sys.stdin.read().split())
t = int(next(read))

for i in range(t): 
    n = int(next(read))
    s = int(next(read))
    lista = [[] for _ in range(n)]
    for j in range(n): 
        g = int(next(read))
        for k in range(g): 
            v = int(next(read))
            p = int(next(read))
            lista[j].append((v,p))

    riesgos = [float ('inf')] * n 
    p = [-1] * n 
    riesgos[s] = 0
    cola = [(0,s)]

    while cola: 
        ru, u = heapq.heappop(cola)

        if ru > riesgos[u]: 
            continue 

        for v, c in lista[u]: 
            nuevo = ru+c 

            if nuevo < riesgos[v]: 
                riesgos[v] = nuevo 
                p[v] = u 
                heapq.heappush(cola,(nuevo, v))

    for i in range(n):
        if i == s or riesgos[i] == float('inf'): 
            continue 
        print(f"{i}:") 
        print(f"riesgo {riesgos[i]}")

        camino = []
        actual = p[i]
        while actual != -1:
            camino.append(str(actual))
            actual = p[actual]
        print(" <- ".join(camino))
