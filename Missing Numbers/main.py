arr = [7,2,5,3,5,3]
brr = [7,2,5,4,6,3,5,3,3,3]

l = []
p = []
for i in brr:
    q = 0
    if(i not in p):
        
        s = brr.count(i)
        t = arr.count(i)
        if(s>t):
            q = s-t
            for w in range(0,q):
                l.append(i)
        p.append(i)
        
        
    if((i not in arr) and (i not in p)):
        l.append(i)
        
        
        
k = sorted(l)
print(k)
