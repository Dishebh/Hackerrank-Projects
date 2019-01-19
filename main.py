s = 'ovyvzvptyvpvpxyztlrztsrztztqvrxtxux'

n = len(s)

a = ''
l = []
k = []
p = []
q = []
for i in range(0,n):
    a = s[i]+a
    l.append(ord(s[i]))


for i in a:
    k.append(ord(i))
    
for i in range(0,n-1):
    
    p.append(abs(l[i+1]-l[i]))
    q.append(abs(k[i+1]-k[i]))
    

if(p == q):
    print('Funny')
else:
    print('Not Funny')


    