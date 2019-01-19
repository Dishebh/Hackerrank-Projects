s = 'aaa'

a = s[::-1]
if(a == s):
    print(-1)

else:
    for i in range(0,len(s)):
        k = s
        k = k[:i] + k[i+1:]
        p = k[::-1]
    
    
        if(p == k):
            print(i)
            break
        k = ''
        p = ''
    
