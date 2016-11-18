x1,y1,r,x2,y2=[int(x) for x in input().split()]
if((x2-x1)**2 + (y2-y1)**2 < r*r):
    print("YES")
else:
    print("NO")
