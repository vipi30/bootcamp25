import sys 

read = sys.stdin.read().split()
n = int(read[0])
if n == 0: 
    print(0)
    exit 

lista = [0] * (n+1)
for i in range(2, n+1): 
    ans = lista[i-1] + 1 
    
    if i % 2 == 0: 
        ans = min(ans, lista[i//2] + 1)
    if i % 3 == 0:
        ans = min(ans, lista[i//3] + 1)
    lista[i] = ans
print(lista[n])
