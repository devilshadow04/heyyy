#Write a program to determine if 3 distinct points create an acute, right, obtuse triangle or a straight line, given the coordinates of the points

import math
ax, ay, bx, by, cx, cy = [float(i) for i in input().split()]

AB = math.sqrt((bx-ax)**2 + (by-ay)**2)
BC = math.sqrt((cx-bx)**2 + (cy-by)**2)
CA = math.sqrt((ax-cx)**2 + (ay-cy)**2)

if AB + BC == CA:
    print("3 points create a straight line")
elif AB**2 + BC**2 == CA**2 or AB**2 + CA**2 == BC**2 or CA**2 + BC**2 == AB**2:
    print("3 points create a right triangle")
elif AB**2 + BC**2 > CA**2 or CA**2 + BC**2 > AB**2 or AB**2 + CA**2 > BC**2:
    print ("3 points create an obtuse triangle")
else:
    print ("3 points create an acute triangle")
