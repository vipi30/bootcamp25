import sys 

read = sys.stdin.read().split()
n = int(read[0])
k = int(read[1])
modulo = 10**9+7 
lista = [0] * (n+1)
lista[1] = 1
suma = 1

for i in range(2,n+1): 
    lista[i] = suma%modulo 
    suma += lista[i]

    if i - k >=1: 
        suma -= lista[i-k]

    suma %= modulo 
print(lista[n])

