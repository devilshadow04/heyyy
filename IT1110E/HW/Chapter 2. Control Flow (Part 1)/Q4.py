#Write a program to input basic salary of an employee and calculate gross salary according to given conditions.

basic_salary = int(input())

if basic_salary <= 10000:
    HRA = 0.2
    DA = 0.8
elif basic_salary <= 20000:
    HRA = 0.25
    DA = 0.9
else:
    HRA = 0.3
    DA = 0.95

da = basic_salary * DA
hra = basic_salary * HRA

gross_salary = basic_salary + da + hra

print("%.2f" % gross_salary)

