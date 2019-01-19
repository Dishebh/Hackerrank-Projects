s = 'fdhlvosfpafhalll'

n = len(s)

k = 0
if(n%2 != 0):
    print(-1)
else:
    a = s[:int(n/2)]
    b = s[int(n/2):]
    
    for i in a:
        if(i not in b) or (a.count(i)!=b.count(i)):
            print(i)
            k+=1
           
    print(a)
    print(b)       
            
    print(k)
