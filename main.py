s = 'akakak'

l = ''
k = list(str(s))
z = 0
p = ''
for i in range(0,len(k)):
    if(k.count(i)%2 == 0):
        l=l+k[i]+k[i]
        k.pop(i)
    if(len(l) == 4):
        print(l)
        l = ''
        z+=1



print(z)