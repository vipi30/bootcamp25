import sys

def find(i):
    if p[i] == i:
        return i
    p[i] = find(p[i])
    return p[i]

def union(i, j):
    ri = find(i)
    rj = find(j)
    if ri != rj:
        p[ri] = rj
        return True
    return False

read = sys.stdin.read().split()
n = int(read[0])
m = int(read[1])

caminos = []
indice = 2
for i in range(1, m+1):
    u = int(read[indice])
    v = int(read[indice+1])
    w = int(read[indice+2])
    caminos.append((w, u, v, i))
    indice += 3

caminos.sort()
p = list(range(n+1))
selec = []

for w, u, v, original in caminos:
    if union(u, v):
        selec.append(original)

print(len(selec))
for camino in selec:
    print(camino)
