'''
+ pr id 
- id 
!

pr -> prioridad
id -> identificación

- heap priority queue -> lo ordena según la prioridad (por defecto lo hace de menor a mayor) 

- set() -> 
'''
import sys, heapq

read = iter(sys.stdin.read().split())
q = int(next(read))

pq = [] #cola
done = set()

for i in range(q): 
    c = next(read)
    if c == "+": 
        pr = int(next(read))
        id_ = int(next(read))
        heapq.heappush(pq, (-pr, id_)) #meto pr e id como un par en la priority queue. El signo "-" para que lo coja de mayor a menor y no de menor a mayor, que es lo que hace por defecto. 

    if c == "-": 
        id_ = int(next(read))
        done.add(id_)
        print(id_)

    if c == "!": 
        while pq and pq[0][1] in done: 
            heapq.heappop(pq)
        pr, id_ = heapq.heappop(pq)
        print(id_)
