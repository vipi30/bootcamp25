import sys 

def rangos(l, r): 
    l += tamaño 
    r += tamaño 

    l_op, l_cl = 0, 0
    r_op, r_cl = 0, 0
    
    while l <= r:
        if l % 2 == 1: 
            if l_op < a2[l]:
                mnuevo = l_op  
            else: 
                mnuevo = a2[l]

            l_op = l_op + a1[l] - mnuevo
            l_cl = l_cl + a2[l] - mnuevo
            l += 1

        if r % 2 == 0: 
            if a1[r] < r_cl:
                mnuevo = a1[r] 
            else: 
                mnuevo = r_cl

            r_op = a1[r] + r_op - mnuevo
            r_cl = a2[r] + r_cl - mnuevo
            r -= 1

        l //= 2
        r //= 2
    
    if l_op < r_cl:
        m_final = l_op 
    else: 
        m_final = r_cl

    total_op = l_op + r_op - m_final
    total_cl = l_cl + r_cl - m_final

    return total_op + total_cl

read = sys.stdin.read().split() 
s = read[0]
n = len(s)
m = int(read[1])

tamaño = 1
while tamaño < n: 
    tamaño *= 2

a1 = [0] * (2 * tamaño)
a2 = [0] * (2 * tamaño)

for i in range(n): 
    if s[i] == '(': 
        a1[tamaño+i] = 1
    else: 
        a2[tamaño+i] = 1

for i in range(tamaño - 1, 0, -1): 
    izq, der = 2 * i, 2 * i + 1
    if a1[izq] < a2[der]: 
        mnuevo = a1[izq] 
    else: 
        mnuevo = a2[der]

    a1[i] = a1[izq] + a1[der] - mnuevo
    a2[i] = a2[izq] + a2[der] - mnuevo 

res = []
p = 2

for i in range(m): 
    l = int(read[p]) - 1
    r = int(read[p + 1]) - 1
    p += 2 

    rango_len = r - l + 1
    s = rangos(l, r)
    res.append(str(rango_len-s))

sys.stdout.write('\n'.join(res)+'\n')
