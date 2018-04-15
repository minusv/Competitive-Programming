def check(ar,n):
    ar.insert(0,0)
    n=n+1
    j=0
    for i in range(1,n):
        d=ar[i]-ar[i-1]
        if d>j:
            j=d
    print(j)
        
t=int(input())
for i in range(t):
    n=int(input())
    ar=list(map(int,input().split()))
    check(ar,n)