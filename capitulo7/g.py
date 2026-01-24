import sys 

primera_linea = sys.stdin.readline()
q = int(primera_linea)
notas = [[] for _ in range(1000001)]
v = [True] * 1000001

for _ in range(q): 
    linea = sys.stdin.readline() 
    query = linea.split()
    t = query[0]
    n = int(query[1])

    if t == '+': 
        nombre = query[2]
        notas[n].append(nombre)
    else: 
        v[n] = False 

res = []
for j in range(1, 1000001): 
    if v[j]: 
        res.append(str(j))
        for k in range(len(notas[j]) - 1, -1, -1): 
            res.append(notas[j][k])

sys.stdout.write('\n'.join(res) + '\n')
