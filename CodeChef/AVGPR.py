def check(n,ar):
    av=[]
    c=0
    for i in range(n):
        n1=ar[i]
        for j in range(i+1,n):
            avg=(n1+ar[j])/2
            av.append(avg)
    print(ar,av)
t=int(input())
for i in range(t):
    n=int(input())
    ar=list(map(float,input().split()))
    ar.sort()
    check(n,ar)