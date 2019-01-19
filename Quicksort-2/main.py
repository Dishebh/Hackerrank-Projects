ar = [5,8,1,3,7,9,2]
m = len(ar)

def sort(arr):
    m = len(arr)
    l = []
    k = []
    p = arr[0]
    for i in range(0,m):
        if(arr[i]>p):
            l.append(arr[i])
        elif(arr[i]<p):
            k.append(arr[i])
            
    print(l)
    print(k)
    sort(l)
    sort(k)
    
a = sort(ar)

        
        
