#N pins were placed in one row, numbered from left to right with numbers from 1 to N.
#Then K balls were thrown along this row, while the i-th ball knocked down all pins with numbers from lᵢ to rᵢ
#inclusive. Your task is to determine which pins are left.

n, k = map(int, input().split())
a = []
for i in range(n):
    a.append("I")
for j in range(k):
    l, r = map(int, input().split())
    for m in range(l-1, r):
        a[m] = '.'
for p in range(len(a)):
    print(a[p], end = '')