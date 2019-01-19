arr = [3,-1,4,2,-1]
L = 3
R = 4

arr[L-1:R] = sorted(arr[L-1:R])
sub_list = []
l=[]
for i in range(0,len(arr)+1):
    
    for j in range(i+1,len(arr)+1):
        l = arr[i:j]
        sub_list.append(l)
    
max=l[0]    
for i in range(0,len(sub_list)):
    s = 0
    for j in sub_list[i]:
        s+=j
    l.append(s)
    
    if(max<l[i]):
        max=l[i]
print(max)