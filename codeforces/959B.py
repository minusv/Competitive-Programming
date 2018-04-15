n,k,m=list(map(int,input().split()))
s=input().split()
c=list(map(int,input().split()))
gr={}
grd={}
for i in range(k):
    inp=list(map(int,input().split()))
    inp.remove(inp[0])
    grd[i+1]=[]
    for x in inp:
        gr[x]=i+1
        grd[i+1].append(c[x-1])
mes=input().split()
su=0
for i in range(m):
    t=s.index(mes[i])+1
    group=gr[t]
    su=min(grd[group])+su
print(su)