total,lose=[int(x) for x in input().split()]

A=[[0 for x in range(2)] for y in range(total)]

i=0
tot1=total
luck=0

B=[0]*total

while(total!=0):
    total=total-1
    A[i][0],A[i][1]=[int (x) for x in input().split()]
    if(A[i][1]==0):
        luck=luck+A[i][0]

    else:
        B.append(A[i][0])

    i=i+1

#input's over
#time to work with important ones

B=sorted(B,reverse=True)

for k in range(lose):
    luck=luck+B[k]

for i in range(lose,tot1):
    luck=luck-B[i]

print(luck)
