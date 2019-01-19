l = 10
r = 15

max = l^l
for i in range(l,r+1):
    for j in range(l,r+1):
        
        if(max<i^j):
            max = i^j
            
print(max)
