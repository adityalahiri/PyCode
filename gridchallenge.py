t=int(input())

while(t!=0):
    t=t-1
    c=0
    n=int(input())
    #A=[[input() for x in range(n)]for y in range(n)]
    A=[list(input()) for x in range(n)]

    for i in range (n):
        A[i].sort()

    #now that row's are sorted
    #got to see the column's sorted or not

    for i in range(n):
        for j in range(n-1):
            if (A[j][i]>A[j+1][i]):
                c=1
                break
    if(c==1):
        print("No")
    else:
        print("Yes")
