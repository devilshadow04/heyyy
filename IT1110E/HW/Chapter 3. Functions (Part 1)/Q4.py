#Consider the following sequence:
#a0=0, a1=1, an=2an-1 + an-2
#Write a function calculate( n ) that takes a non-negative integer n as input and outputs the value of an.

def calculate(n):
    fi = 0
    fj = 1
    i = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        while fj > 0:
            x = 2*fj + fi
            fi = fj
            fj = x
            i = i + 1
            if i == int(n):
                break
        return x

