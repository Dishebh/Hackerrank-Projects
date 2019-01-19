d = {1:'one', 2:"two" }
from array import array
d1 = {3:"three"}
d.update(d1)

print(d)
for key, value in d.items():
    print(key,' : ',value)
    
k = d.values()
print(list(k), end=' ')
arr = array('a')
print(arr)
