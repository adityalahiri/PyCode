t=int(input())

def gcd(a,b):
    if (b==0):
        return a
    else:
        r=a%b
        return gcd(b,r)

while(t!=0):
    min=0
    hcf=0
    lcm=0
    t=t-1
    n=int(input())
    arr=[int(y) for y in input().split()]
    for i in range (n-1):
        for j in range(i+1,n):
            if(i==0 and j==1):
                min=arr[0]*arr[1]/gcd(arr[0],arr[1])
            lcm=arr[i]*arr[j]/gcd(arr[i],arr[j])
            if(lcm<min):
                min=lcm
    print(int(min))
