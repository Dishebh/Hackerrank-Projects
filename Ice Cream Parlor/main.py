m = 4
arr = [2,2,4,3]
n = len(arr)

l = []
s = 0
for i in range(0,n):
    for j in range(i+1,n):
        s = arr[i]+arr[j]
        if(s == m):
            l.append(i+1)
            l.append(j+1)
            
print(l)
