import sys 

read = sys.stdin.read().split() 
q = int(read[0])
qu = read[1:]

modulo = 10**9 + 7 
maximo = 300000

fibonacci = [0] * (maximo + 1)
#primeros n 
fibonacci[0] = 0 
fibonacci[1] = 1
for i in range(2, maximo+1): 
    fibonacci[i] = (fibonacci[i-1] + fibonacci[i-2]) % modulo

res = [] 
for i in range(q): 
    n = int(qu[i])
    res.append(str(fibonacci[n]))

sys.stdout.write('\n'.join(res))



