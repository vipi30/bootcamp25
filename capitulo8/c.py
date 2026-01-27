import sys

def find(i, p): 
    if p[i] == i: 
        return i  
    p[i] = find(p[i], p)
    return p[i]

read = sys.stdin.readline()
n = int(read.strip())
p = list(range(n+1))
while True: 
    cs = sys.stdin.readline().split()
    v = int(cs[1])
    u = int(cs[2])

    ru = find(u, p)
    rv = find(v, p)

    if ru != rv: 
        print('SI')
        sys.stdout.flush() #para q no se quede congelado
        p[ru] = rv
    else: 
        print('NO')
        sys.stdout.flush() 
        break 


