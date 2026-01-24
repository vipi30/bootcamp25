import sys

def solve():
    read = iter(sys.stdin.read().split())
    q = int(next(read))
    
    maximo = q + 5
    l = [0] * maximo
    r = [0] * maximo
    v = [''] * maximo
    
    principio, final = 0, 1
    r[principio], l[final] = final, principio
    
    c = principio
    anchor = principio
    s = False
    nxt_id = 2 
    
    ans = []

    for _ in range(q):
        comando = next(read)
        
        if (comando == 'INSERT' or comando == 'DELETE') and s and c != anchor:
            ls = rs = c
            encontrado = ""
            while True:
                if ls == anchor:
                    encontrado = "left"
                    break
                if rs == anchor:
                    encontrado = "right"
                    break
                if ls != principio: ls = l[ls]
                if rs != final: rs = r[rs]
            
            if encontrado == "left":
                derecha = r[c]
                r[anchor] = derecha
                l[derecha] = anchor
                cur = anchor
            else:
                derecha = r[anchor]
                r[c] = derecha
                l[derecha_de_todo] = c
            
            s = False

        if comando == 'INSERT':
            ch = next(read)
            sel_active = False 
            
            nuevo = nxt_id
            nxt_id += 1
            v[nuevo] = ch
            
            derecha = r[c]
            r[c] = nuevo
            l[nuevo] = c
            r[nuevo] = derecha
            l[derecha] = nuevo
            
            ch = nuevo
            anchor = ch
            
        elif comando == 'DELETE':
            if not s:
                target = r[c]
                if target != final:
                    derecha_objetivo = r[objetivo]
                    r[c] = derecha_objetivo
                    l[derecha_objetivo] = c
            s = False
            anchor = c

        elif comando == 'MOVE_LEFT':
            if c != principio:
                c = L[cur]
            if not s: 
                anchor = c
            
        elif comando == 'MOVE_RIGHT':
            if r[c] != final:
                c = r[c]
            if not s: 
                anchor = c
            
        elif comando == 'SELECT':
            if s:
                s = False
            else:
                s = True
                anchor = c
                
        elif comando == 'BEGIN':
            c = principio
            if not s: 
                anchor = c
            
        elif comando == 'END':
            c = l[final]
            if not s: 
                anchor = c
            
        elif comando == 'PRINT':
            res = []
            if c == principio: 
                res.append('|')
            nodo = r[principio]
            while nodo != final:
                res.append(v[nodo])
                if nodo == c:
                    res.append('|')
                nodo = r[nodo]
            ans.append("".join(res))

    sys.stdout.write("\n".join(ans) + "\n")
solve()
