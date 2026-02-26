#recurrencia simple: an = an - 1 + an - 2 + an - 3 
import sys 
read = sys.stdin.read().split()
n = int(read[0])
a, b, c = map(int, read[1:])

res = [a,b,c] #guardo los primeros números de la secuencia 

for i in range(3, n): 
    sig = res[i-1] + res[i-2] + res[i-3]
    res.append(sig) 
print(*res)
    
