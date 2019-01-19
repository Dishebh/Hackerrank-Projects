a = [3,3,9,9,5]
m = 7

p = 0
l = []
sublist = [[]] 
      
# first loop  
for i in range(len(a) + 1): 
          
    # second loop  
    for j in range(i + 1, len(a) + 1): 
              
        # slice the subarray  
        sub = a[i:j] 
        sublist.append(sub) 
              
      
for i in sublist:
    if(i is not None):
        p = sum(i)
        
        k = p%m
        l.append(k)
    p = 0
print(max(l))