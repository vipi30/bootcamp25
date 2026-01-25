import sys 

read = sys.stdin.read().split() 
n = int(read[0])
alumnos = [int(x) -1 for x in read[1:]]

res = [] 
for a in range(n): 
    v = [False] * n
    actual = a 

    while not v[actual]: 
        v[actual] = True
        actual = alumnos[actual]
    res.append(actual+1)
print(*res)
