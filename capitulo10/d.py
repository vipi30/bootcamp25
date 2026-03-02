import sys 

n, a, b, c = map(int, sys.stdin.read().split())
tabla = [-float('inf')]*(n+1)
tabla[0] = 0

for i in range(n+1): 
    for op in [a,b,c]: 
        if i >= op: 
            tabla[i] = max(tabla[i], tabla[i-op]+1)

print(int(tabla[n]))

