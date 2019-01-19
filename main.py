B = [1,2,3]
n = len(B)

A = []
l = []

for i in range(0,n):
    for k in range(0,n):
        for j in range(1,max(B)+1):
            if(j<=B[k]):
                l.append(j)
            #break
        #break
        
        
    A.append(l)    
    l = []
    


print(A)