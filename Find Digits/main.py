n = 1012

k = list(str(n))
z = 0
for i in range(0,len(k)):
    if(k[i] == '0'):
        pass
    elif(n%int(k[i]) == 0):
        z+=1
        
print(z)
