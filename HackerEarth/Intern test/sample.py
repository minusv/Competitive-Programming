t=int(input())
for i in range(t):
    arr=[]
    n=int(input())
    for i in range(n):
        a=list(map(int,input().split()))
        arr.append(a)
    s=check(arr,n)
    print(s) 