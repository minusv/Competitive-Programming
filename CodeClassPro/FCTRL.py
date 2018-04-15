import math
def zer(num):
    p=1
    count=0
    while(True):
        temp=math.floor(num/(5**p))
        if temp>=1:
            count=count+temp
            p=p+1
        else:
            break
    print(count)

t=int(input())
for i in range(t):
    num=int(input())
    zer(num)