t=int(input())

while(t!=0):
    c=0
    f=0
    th=0
    t-=1
    N=int(input())
    threes=[x for x in range(0,N+1,5)]
    for i in range(len(threes)):
        th=threes[i]
        f=N-th
        if(f%3==0):
            print('5'*f+'3'*th)
            c=1
            break

    if(N%5==0 and c==0):
        print('3'*N)
    elif(c==0):
        print(-1)
