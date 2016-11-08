n=int(input())
arr=[]
arr.append(int(x) for x in input().split())
while(n!=0):
    n=n-1
    arr.append(int(input()))
arr=sorted(arr,reverse=True)
print (arr[0]*arr[1])
