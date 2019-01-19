orders = [[8,1],[4,2],[5,6],[3,1],[4,3]]
n = len(orders)

t = 0
l = []
p = []
q = []
r = []
for i in range(0,n):
    l.append([])
    l[i].append(orders[i][0])
    for j in orders[i]:
        t = t+j
        
    l[i].append(t)
    t = 0
    

for i in range(0,n-1):
    
    p.append(l[i][1])
        
q = sorted(p)
for i in range(0,n):
    r.append()
