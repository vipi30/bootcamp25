import sys 

read = sys.stdin.read().split()
n = int(read[0])
m = int(read[1])
modulo = 10**9+7
tabla = []
ind = 2

for i in range(n): 
    tabla.append([int(x) for x in read[ind:ind+m]])
    ind += m 

lista = [[0] * m for _ in range(n)]
lista[0][0] = 1

for i in range(n): 
    for j in range(m): 
        if lista[i][j] == 0: 
            continue

        t = tabla[i][j]
        if t == 0: 
            continue 

        if i + t < n: 
            lista[i+t][j] = (lista[i+ t][j] + lista[i][j]) % modulo 

        if j + t < m: 
            lista[i][j + t] = (lista[i][j + t] + lista[i][j]) % modulo

print(lista[n-1][m-1])
