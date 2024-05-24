#It is known that 8 queens can be placed on an 8 × 8 board so that they do not beat each other.
#You are given the arrangement of 8 queens on the board, determine if there is a pair of them
#that can beat each other.

def can_beat(q1, q2):
    if q1[0] == q2[0] or q1[1] == q2[1]:
        return True
    if abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
        return True
    return False

def has_beating_queen(arr):
    for i in range(8):
        for j in range(i+1, 8):
            if can_beat(arr[i], arr[j]):
                return True
    return False

n = int(input())

for _ in range(n):
    arrangement = []
    for _ in range(8):
        x, y = map(int, input().split())
        arrangement.append((x-1, y-1))
    if has_beating_queen(arrangement):
        print('YES')
    else:
        print('NO')

