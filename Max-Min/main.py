arr = [10,100,300,200,1000,20,30]
k = 3

l = sorted(arr)
p = []

for i in range(0,k):
    p.append(l[i])
    
    

print(max(p) - min(p))
