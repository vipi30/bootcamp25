import sys 

read = sys.stdin.read().split()
n = int(read[0])
m = int(read[1])
p = read[2:]
lista = [[0] * m for _ in range(n)]
modulo = 10**9+7

if p[0][0] == '.': 
    lista[0][0] = 1

for i in range(n): 
    for j in range(m): 
        if p[i][j] == '#': 
            lista[i][j] = 0
            continue 
        if i > 0: 
            lista[i][j] = (lista[i][j] + lista[i-1][j]) % modulo 

        if j > 0:
            lista[i][j] = (lista[i][j] + lista[i][j-1]) % modulo 
print()
print(lista[n-1][m-1])
