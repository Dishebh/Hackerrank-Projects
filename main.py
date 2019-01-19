'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

A = [[1,3,4],[2,2,3],[1,2,4]]
s=0
n=len(A)
for i in range(len(A)):
    for j in A[i]:
        s=s+(2+ (4*j))
        
for i in range(len(A)):
    for j in A[i]:
        if((j == 0) or (j == n-1)):
            s=s-((A[i+1][j]) + (A[i][j+1]))
print(s)
            