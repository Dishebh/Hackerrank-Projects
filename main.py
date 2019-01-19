price = [5,10,3]
n = len(price)

min = None
for i in range(0,n):
    s = 0
    for j in range(i+1,n):
        s = price[i]-price[j]
        if(min is None):
            if(s>0):
                min = price[i]-price[j]
        if(s==0):
            print(s)
        elif(s>0):
            
            if(min>s):
                min = s
                
print(min)