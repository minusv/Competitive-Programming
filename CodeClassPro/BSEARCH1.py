def bs(arr, l, r, x):
    while l<=r:
        mid=int((l+r)/2);
        if arr[mid]==x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r=mid-1
    return -1

n,t = list(map(int,input().split()))
arr = list(map(int,input().split()))
r = len(arr)-1
l = 0
for i in range(t):
    x=int(input())
    k=bs(arr,l,r,x)
    print(k)