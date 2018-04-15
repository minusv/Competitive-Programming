n=int(input())
c=list(map(int, input().split()))
w=list(map(int, input().split()))
d={1:[],2:[],3:[]}
for i in range(n):
    d[w[i]].append(c[i])

if d[3]==[]:
    s12=min(d[1])+min(d[2])
    print(s12)
elif d[2]==[] and d[1]==[]:
    print(min(d[3]))
else:
    s1=0
    s2=0
    if d[1]!=[]:
        s1=min(d[1])
    if d[2]!=[]:
        s2=min(d[2])
    if s1==0 or s2==0:
        print(min(d[3]))
    else:
        s12=s1+s2
        s3=min(d[3])
        print(min(s12,s3))