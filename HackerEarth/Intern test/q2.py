import bisect
def check(temp,h,n):
    arr=temp
    c=arr.count(h)
    i=arr.index(h)
    pos=i+1
    s=pos+c-1
    
    print(n-s+1)
    '''while(True):
        i = arr.index(h)
        arr.remove(h)
        if arr[i] != h:
            print(len(arr)-i)
            break'''

n = int(input())
arr = list(map(int,input().split()))
k = int(input())
t=[]
arr.sort()
print(arr)

for i in range(k):
    h = int(input())

    p = bisect.bisect_right(arr,h)
    print(h,n-p)
