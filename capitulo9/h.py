import sys

def solve():

    def actualizar(indice):
        p = n + indice
        
        actual = maximo[p]
        nuevo = 1 - actual
        
        maximo[p] = nuevo
        pre[p] = nuevo
        suf[p] = nuevo
        
        while p > 1:
            p //= 2 
            izq = 2 * p
            der = 2 * p + 1
            
            longitud[p] = longitud[izq] + longitud[der]
            
            if maximo[izq] == longitud[izq]:
                pre[p] = longitud[izq] + pre[der]
            else:
                pre[p] = pre[izq]
                
            if maximo[der] == longitud[der]:
                suf[p] = longitud[der] + suf[izq]
            else:
                suf[p] = suf[der]
                
            maximo[p] = max(maximo[izq], maximo[der], suf[izq] + pre[der])

    read = iter(sys.stdin.read().split())
    n = int(next(read))
    q = int(next(read))

    bol = []
    while len(bol) < n:
        ch = next(read)
        for char in ch:
            bol.append(char)
            
    arr = [1 if c == 'F' else 0 for c in bol]

    maximo = [0] * (2 * n)  
    pre = [0] * (2 * n) 
    suf = [0] * (2 * n) 
    longitud = [0] * (2 * n) 
    
    for i in range(n):
        val = arr[i]
        indice = n + i
        maximo[indice] = val
        pre[indice] = val
        suf[indice] = val
        longitud[indice] = 1 
    
    for i in range(n - 1, 0, -1):
        izq = 2 * i
        der = 2 * i + 1
        longitud[i] = longitud[izq] + longitud[der]
        
        if maximo[izq] == longitud[izq]: 
            pre[i] = longitud[izq] + pre[der]

        else:
            pre[i] = pre[izq]
            
        if maximo[der] == longitud[der]:
            suf[i] = longitud[der] + suf[izq]

        else:
            suf[i] = suf[der]
            
        maximo[i] = max(maximo[izq], maximo[der], suf[izq] + pre[der])

    res = []
    for _ in range(q):
        type_q = next(read)
        
        if type_q == 'c':
            indice = int(next(read)) - 1 
            actualizar(indice)
        else:
            l = int(next(read)) - 1 
            r = int(next(read)) - 1
            l_node = n + l
            r_node = n + r
            
            res_l = (0, 0, 0, 0) 
            res_r = (0, 0, 0, 0)
            
            while l_node <= r_node:
                if l_node % 2 == 1:
                    curr = (maximo[l_node], pre[l_node], suf[l_node], longitud[l_node]) #contiene los datos del bloque actual
                    
                    lmx, lpre, lsuf, llen = res_l
                    rmx, rpre, rsuf, rlen = curr
                    
                    new_len = llen + rlen
                    new_pre = lpre + rpre if lmx == llen else lpre
                    new_suf = rsuf + lsuf if rmx == rlen else rsuf
                    new_mx = max(lmx, rmx, lsuf + rpre)
                    
                    res_l = (new_mx, new_pre, new_suf, new_len)
                    l_node += 1
                
                if r_node % 2 == 0:
                    curr = (maximo[r_node], pre[r_node], suf[r_node], longitud[r_node])
                    #uno con nuevo bloque
                    lmx, lpre, lsuf, llen = curr       
                    rmx, rpre, rsuf, rlen = res_r
                    
                    new_len = llen + rlen
                    if lmx == llen:
                        new_pre = lpre + rpre  
                    else: 
                        new_pre = lpre
                    if rmx == rlen:
                        new_suf = rsuf + lsuf  
                    else:
                        new_suf = rsuf

                    new_mx = max(lmx, rmx, lsuf + rpre)
                    
                    res_r = (new_mx, new_pre, new_suf, new_len)
                    r_node -= 1
                
                l_node //= 2
                r_node //= 2

            #uno para saber la racha máxima total en el rango
            lmx, lpre, lsuf, llen = res_l
            rmx, rpre, rsuf, rlen = res_r
            
            ans = max(lmx, rmx, lsuf + rpre)
            res.append(str(ans))

    print('\n'.join(res))

solve()
