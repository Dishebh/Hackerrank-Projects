p = 20
d = 3
m = 6
s = 80


count = 0
while(s >= p):
    count+=1
    s-=p
    p = max(p-d,m)
    
print(count)