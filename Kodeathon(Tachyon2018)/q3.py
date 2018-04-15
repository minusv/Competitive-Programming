def palin(s):
    k=list(s)
    k.reverse()
    k=str(k)
    if k==str(list(s)):
        return(1)
    else:
        return(0)

d={}
def cuts(s):
    cut=0
    for i in range(1,len(s)):
        lesol=0
        resol=0
        left=s[0:i]
        right=s[i:len(s)]
        if left in d:
            lesol=d[left]
        else:
            lesol=cuts(left)
            d[left]=lesol
        if right in d:
            resol=d[right]
        else:
            resol=cuts(right)
            d[right]=resol
        cut=min(1+lesol+resol,cut)
    return(cut)

s="cdcdddcdadcdcdcd"

print(cuts(s))
print(d)