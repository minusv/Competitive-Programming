def check(d):
    m=0
    for i,j in d.items():
        if j>m:
            m=j
    print(m)
d={}        
n=int(input())
for i in range(n):
    wr=input()
    wr=list(wr)
    wr.sort()
    s=str(wr)
    try:
        d[s]=d[s]+1
    except KeyError:
        d[s]=1
    
check(d)