arr = [0,-3,6,4,-10,8,-5,2,-7]
n = len(arr)

k = arr[0]
l = []
p = []
for i in range(0,n):
    if(arr[i]>k):
        l.append(arr[i])
    elif(arr[i]<k):
        p.append(arr[i])
        
p.append(k)
print(p+l)