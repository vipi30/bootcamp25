import sys 

read = sys.stdin.read().splitlines()
t = int(read[0])
linea = 1 
for i in range(t): 
    if linea >= len(read): 
        break 

    s = read[linea]
    linea+=1
    n = len(s)
    c = []
    ind = []

    for i in range(n): 
        if s[i] != ' ':
            c.append(s[i].lower())
            ind.append(i)

    m = len(c)
    maximo = -1 
    mejor = ''

    for j in range(2 * m-1): 
        izq = j // 2
        der = izq + (j % 2)

        while izq >= 0 and der < m and c[izq] == c[der]: 
            actual = der-izq + 1 
            inicio = ind[izq]
            fin = ind[der]
            sub = s[inicio : fin+1]

            if actual > maximo: 
                maximo = actual 
                mejor = sub 
            elif actual == maximo: 
                if sub < mejor: 
                    mejor = sub 

            izq -= 1
            der += 1

    print(mejor)
