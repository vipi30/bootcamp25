#dp
#sparse table
import sys

def solve():
    read = iter(sys.stdin.read().split())
    t = int(next(read))
    
    res = []

    for i in range(t):
        n = int(next(read))
        a = [int(next(read)) for _ in range(n)]
    
        p_max = n.bit_length()
        m = [None] * p_max
        m[0] = a 

        for k in range(1, p_max):
            m[k] = [0] * (n - (1 << k) + 1)
            anterior = m[k-1]
            salto = 1 << (k - 1)

            for i in range(n - (1 << k) + 1):
                valor1 = anterior[i]
                valor2 = anterior[i + salto]

                if valor1 < valor2:
                    m[k][i] = valor1
                else:
                    m[k][i] = valor2
        
        p = int(next(read))

        for _ in range(p):
            l = int(next(read)) - 1
            r = int(next(read)) - 1
            
            tamaño = r - l + 1
            k = tamaño.bit_length() - 1
            
            v1 = m[k][l]
            v2 = m[k][r - (1 << k) + 1]

            if v1 < v2: 
                ans = v1  
            else:
                ans = v2

            res.append(str(ans))
            
    sys.stdout.write("\n".join(res) + "\n")

solve()
