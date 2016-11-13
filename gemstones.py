n=int(input())
A=[0]*26
B=[]

for i in range(n):
    B.append(input())

for i in range(26):
    ch=chr(i+97)
    for j in range(n):
        if ch in B[j]:
            A[i]=A[i]+1

c=0
for i in range(26):
    if(A[i]==n):
        c=c+1
print(c)
