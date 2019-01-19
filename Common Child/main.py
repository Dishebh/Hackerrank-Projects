s1 = 'ABCDEF'
s2 = 'FBDAMN'

p = sorted(s1)
q = sorted(s2)

l = ''
k = 0
for i in s1:
    if(i in s2):
        l+=i
        k+=1
if(p == q):
    k-=1
        
print(p)
print(q)
        
print(l)
