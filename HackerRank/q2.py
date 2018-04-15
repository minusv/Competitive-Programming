def check(t,data):
    data.sort()
    print(data)
data=[]    
t=int(input())
for i in range(t):
    a=list(input())
    a.sort()
    data.append(a)

check(t,data)