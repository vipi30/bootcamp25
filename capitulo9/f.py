import sys

def gana(a, b, h):
    if a == b: 
        return a
    is_normal = (h % 2 == 1)
    if (a + 1) % 3 == b:
        if is_normal: 
            return b 
        else:
            return a
    else:
        if is_normal: 
            return a 
        else: 
            return b


read = sys.stdin.read().split()
n = int(read[0])
m = int(read[1])
N = 1 << n 

mapeado = {'piedra': 0, 'papel': 1, 'tijera': 2}
rev = ['piedra', 'papel', 'tijera']

tree = [0] * (2 * N) #segtree
a = [0] * (2 * N)

for i in range(N):
    tree[N + i] = mapeado[read[2 + i]]
    a[N + i] = 0
        
for i in range(N - 1, 0, -1):
    a[i] = a[2 * i] + 1
    tree[i] = gana(tree[2 * i], tree[2 * i + 1], a[i])
        

actual = 2 + N
res = []

for _ in range(m):
    pos = int(read[actual]) - 1 
    nuevo = mapeado[read[actual + 1]]
    actual += 2
    indice = N + pos
    tree[indice] = nuevo
    indice //= 2

    while indice >= 1:
        tree[indice] = gana(tree[2 * indice], tree[2 * indice + 1], a[indice])
        indice //= 2
    
    res.append(rev[tree[1]])
        
sys.stdout.write('\n'.join(res) + '\n')
