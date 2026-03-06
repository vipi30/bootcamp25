import sys 

read = sys.stdin.read().split()
n = int(read[0])
m = int(read[1])
p = []
ind = 2

for j in range(n): 
    p.append([int(x) for x in read[ind:ind+m]])
    ind += m 

for i in range(1,m): 
    p[0][i] += p[0][i-1]

for i in range(1,n): 
    p[i][0] += p[i-1][0]

for i in range(1,n): 
    for j in range(1,m): 
        up = p[i-1][j]
        izq = p[i][j-1] 

        if up > izq: 
            p[i][j] += up 
        else:
            p[i][j] += izq
print(p[n-1][m-1])
