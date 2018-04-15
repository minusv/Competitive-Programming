def check(t,data):
    arr=[]
    for i in range(t):
        arr.append(abs(data[i][1]-data[i][2]))
    m=max(arr)
    ind=arr.index(m)
    print(data[ind][0],m)

data=[]    
t=int(input())
for i in range(t):
     a=list(input().split())
     a[1]=int(a[1])
     a[2]=int(a[2])
     data.append(a)

check(t,data)