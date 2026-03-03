import sys 

read = iter(sys.stdin.read().split())
n = int(next(read))
modulo = 10**9+7 

lista = [0] * (n+1)
lista[0] = 1
for i in range(1, n+1): 
    for d in range(1,7):
        if i - d >=0: 
            lista[i] = (lista[i]+lista[i-d])%modulo 
print(lista[n])
