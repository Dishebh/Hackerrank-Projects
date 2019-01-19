p = [10,100]
x = [5,100]
y = [4]
r = 1
n = len(p)
m = len(y)

a = max(p)
b = p.find(a)
s = sum(p)
for i in range(0,m):
    if(b>=y[i]-1) and (b<=y[i]+1):
        del y[i]
        
        
        
