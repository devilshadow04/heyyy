#Write a Python program to check whether a triangle is Equilateral, Isosceles or Scalene.

a = int(input())
b = int(input())
c = int(input())

if a == b and a == c:
    print("Equilateral")
elif a == b or a == c or b == c:
    print("Isosceles")
else:
    print("Scalene")