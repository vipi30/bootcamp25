import sys

read = sys.stdin.read().split()
indice = 0

t = int(read[indice])
indice += 1

for i in range(t):
    n = int(read[indice])
    m = int(read[indice + 1])
    
    indice += 2
    grados = [0] * (n + 1)
    
    for i in range(m):
        u = int(read[indice])
        v = int(read[indice+1])
        grados[u] += 1
        grados[v] += 1
        indice += 2

    hojas = 0
    no_hojas = 0
    
    for i in range(1, n + 1):
        if grados[i] == 1:
            hojas += 1
        else:
            no_hojas += 1
    
    x = no_hojas - 1
    y = hojas // x
    print(f"{x} {y}")
