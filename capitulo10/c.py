import sys 

read = sys.stdin.read().split() 
t = int(read[0])
p = 1

for i in range(t): 
    m1 = read[p]
    m2 = read[p+1]
    p+=2

    n = len(m1)
    m = len(m2)

    a = list(range(m+1))

    for j in range (1, n+1): 
        actual = [j] * (m+1)
        for k in range(1, m+1): 
            if m1[j-1] == m2[k-1]: 
                actual[k] = a[k-1] 
            else: 
                actual[k] = 1+min(a[k-1], a[k], actual[k-1]) 
        a = actual 
    print(a[m])
