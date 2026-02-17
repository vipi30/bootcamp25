#segment tree iterativo
import sys

read = sys.stdin.read().split()

res = [] 
puntero = 0
t = int(read[puntero])
puntero += 1

for i in range(t): 
    n = int(read[puntero])
    puntero += 1 
    c = read[puntero : puntero + n]
    puntero += n

    tamaño = n
    tree = [0] * (2 * tamaño)

    for j in range(tamaño): 
        tree[tamaño + j] = int(c[j])

    for k in range(tamaño - 1, 0, -1): 
        tree[k] = min(tree[2 * k], tree[2 * k + 1])

    q_ops = int(read[puntero])
    puntero += 1
        
    for _ in range(q_ops):
        tp = read[puntero]
        valor1 = int(read[puntero + 1])
        valor2 = int(read[puntero + 2])
        puntero += 3
            
        if tp == 'Q':
            l = valor1 + tamaño - 1 
            r = valor2 + tamaño  
            min_actual = float('inf')

            while l < r:
                if l & 1: 
                    if tree[l] < min_actual: 
                        min_actual = tree[l]
                    l += 1
                if r & 1:
                    r -= 1
                    if tree[r] < min_actual: 
                        min_actual = tree[r]
            
                l //= 2
                r //= 2
            
            res.append(str(min_actual)) 
                
        else:
            indice = valor1 + tamaño - 1
            nuevo_v = valor2
            tree[indice] = nuevo_v
            idx = indice
            while idx > 1:
                idx //= 2
                nuevo_min_padre = min(tree[2 * idx], tree[2 * idx + 1])
                if tree[idx] == nuevo_min_padre: 
                    break

                tree[idx] = nuevo_min_padre

# 
sys.stdout.write('\n'.join(res) + '\n')
