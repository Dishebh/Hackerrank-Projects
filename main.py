''''T = int(input())
for i in range(T):
    N, a, b = [int(x) for x in input().split()]
'''
N = 3
a = 4
b = 1

l = [0]
l.append(a*N)
l.append(-b*N)
for i in range(1,N+1):
    for j in range(0,N-i):
        l.append(a*(i-j) - b*(N-i-j))
        l.append(a*(N-i-j) - b*(i-j))
        l.append(a*(i-j))
        l.append(-b*(i-j))
        l.append(a*i - b*(i-j))
        
final_list = []
for i in l:
    if(i not in final_list):
        final_list.append(i)
        
print(final_list)
print(len(final_list))

    
        


