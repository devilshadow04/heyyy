#write a program that takes an integer n as input and output the n-th Fibonacci number

n = int(input())
f0 = 0
fn = 1
i = 1
if n == 0:
    print("0")
elif n == 1:
    print("1")
else:
    while fn > 0:
        x = fn + f0
        f0 = fn
        fn = x
        i = i + 1
        if i == int(n):
            break
    print(x)

