c = [1,2,3,4]
n = len(c)
k = 3

cost = 0
person = 0
minCost = 1000
p = 0
for person in range(1,k+1):
    
    for i in range(0,n):
        cost = cost + (person + 1)*c[i]
    if(minCost > cost):
        minCost = cost
            
    p+=1        
            
print(minCost)
