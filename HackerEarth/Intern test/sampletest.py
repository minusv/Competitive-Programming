def check(num):
    for i in range(1,num+1):
        if i%3 == 0 and i%5 != 0:
            print("Fizz")
        elif i%5 == 0 and i%3 != 0:
            print("Buzz")
        elif i%5 == 0 and i%3 == 0:
            print("FizzBuzz")
        else:
            print(i)

t=int(input())
a=list(map(int,input().split()))
for i in a:
    check(i)