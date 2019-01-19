prices = [1,12,5,111,200,1000,10]
k = 50
n = len(prices)

p = sorted(prices)
s = 0
l = []
for i in p:
    s = s+i
    if(s<=k):
        l.append(i)
    
    
    
     
print(len(l))
    
