k = 1
arr = [1,2,3,4]

p = len(arr)
l = 0
for i in range(0,p):
    s = 0
    for j in range(i+1,p):
        s = abs(arr[i]-arr[j])
        if(s == k):
            l+=1
            
            
print(l)