import sys 

read = sys.stdin.read().split() 
puntero = 0

while puntero < len(read): 
    n = int(read[puntero])
    m = int(read[puntero+1])
    puntero += 2

    c = [[False] * (n+1) for _ in range(n+1)]

    for i in range(m): 
        u = int(read[puntero])
        v = int(read[puntero+1])
        c[u][v] = c[v][u]
        c[u][v] = True
        c[v][u] = True
        puntero+= 2

    faltan = []
    for i in range(1, n+1): 
        for j in range(i+1, n+1): 
            if not c[i][j]: 
                faltan.append(f'{i} {j}')

    print(len(faltan))
    print('\n'.join(faltan))

