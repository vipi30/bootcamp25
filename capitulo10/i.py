import sys 

read = sys.stdin.read().split()
n = int(read[0])
m = int(read[1])
lista = [[0] * (m+1) for _ in range(n+1)]
lista[1][1] = 1

for i in range(1, n+1): 
    for j in range(1, m+1): 
        if lista[i][j] > 0: 
            if i+2 <= n and j+1 <=m: 
                lista[i+2][j+1] += lista[i][j]
            
            if i +1 <= n and j+2 <= m: 
                lista[i+1][j+2] += lista[i][j]
print(lista[n][m])
