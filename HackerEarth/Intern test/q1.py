def check(a,cas,k):
    if cas=='L':
        print(a[k]-1)
    else:
        print(a[k-1])
    
t=int(input())
for i in range(t):
    d=list(map(int,input().split()))
    s=input()
    k=list(s)
    di={}
    for i in range(97,123):
        di[chr(i)]=[]
    for i,j in enumerate(k):
        di[j].append(i+1)
    for i in range(d[1]):
        qur=input()
        q=qur.split()
        check(di[q[1]],q[0],int(q[2]))