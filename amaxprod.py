n=int(input())

A =[int(x) for x in input().split()]

A=sorted(A,reverse=True)

pro1,pro2,pro3=1,1,1

#pro1

for i in range(5):
    pro1=pro1*A[i]

#pro2

for i in range(3):
    pro2=pro2*A[i]
for j in range(n-1,n-3,-1):
    pro2=pro2*A[j]

#pro3

for i in range(1):
    pro3=pro3*A[i]
for j in range(n-1,n-5,-1):
    pro3=pro3*A[j]

print(max(pro1,pro2,pro3))
