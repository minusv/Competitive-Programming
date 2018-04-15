def check(sen):
    l=len(sen)
    count=0
    while(True):
        if 'chef' in sen:
            sen=sen.split("chef")
            count=len(sen)+count
            sen=''.join(sen)
        


t=int(input())
for i in range(t):
    sen=input()
    check(sen)