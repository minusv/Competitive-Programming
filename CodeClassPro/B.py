import math

def bs(arr, l, r, x):
    while l<=r:
        mid=l+(r-l)/2;
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r=mid-1
    return -1

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
    return(count)

num=100000000
while(True):
    c=zer(num)
    if c==100000000:
        print(num)
        break
    else:
        num=num+1