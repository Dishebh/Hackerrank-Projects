s1 = 'hi'
s2 = 'world'

k = 0
for i in s1:
    if(i in s2):
        k+=1
        
if(k > 0):
    print('YES')
else:
    print('NO')
