arr = [2,1,3,1,2]
n = len(arr)

k = 0
for i in range(1,n):
    j = i-1
    key = arr[i]
    while((j>=0) and (arr[j]>key)):
        arr[j+1] = arr[j]
        k+=1
        j-=1
    arr[j+1] = key
    
print(k)
print(arr)