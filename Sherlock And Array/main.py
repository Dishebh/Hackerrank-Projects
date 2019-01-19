arr = [0,0,2,0]
n = len(arr)

l = []
k = []
z = 0
for i in range(0,n):
    
    s = 0
    q = 0
    l = arr[0:i]
    k = arr[i+1:n]
    
    for j in l:
        s = s+j
    for p in k:
        q = q+p
        
    if(s == q):
        print('YES')
        z+=1
        
    
    
if(z == 0):
    print('NO')
    











