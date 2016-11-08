N=int(input())
K=int(input())

A=[N]*0

for i in range(N):
    A.append(int(input()))

min=0
diff=0
di=[]

A=sorted(A)

for i in range(N-K+1):
    diff=A[i+K-1]-A[i]
    if(i==0):
        min=diff
    else:
        if(diff<=min):
            min=diff

print(min)
