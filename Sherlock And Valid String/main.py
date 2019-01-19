from collections import Counter

s1 = 'aabbcd'

k = 0
s = list(str(s1))
a = Counter()
a.update(s)

b = Counter()
l = []
for keys in a:
    l.append(a[keys])
    
for key,value in a.most_common(1):
    b.update([value])

print(b)

