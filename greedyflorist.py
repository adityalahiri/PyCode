n,k=[int(x) for x in input().split()]

A=[int(y) for y in input().split()]

cost=0
turn=0
rem=n%k

A=sorted(A,reverse=True)
for i in range(0,n,k):
    if(i<=n-k):
        for j in range(i,i+k):
            cost=cost+(turn+1)*A[j]
        turn+=1

if(rem!=0):
    for i in range(1,rem+1):
        cost=cost+(turn+1)*A[-i]

print(cost)
