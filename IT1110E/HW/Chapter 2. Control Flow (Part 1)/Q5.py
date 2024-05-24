#Write a Python program that reads the type of a vehicle exiting a car park (1 for car, 2 for bus and
#3 for truck) and the number of hours spent in the car park; and calculates the parking fee given the following
#rates (GST included):

type = int(input())
hours = int(input())

if type == 1:
    if hours < 3:
        fee = 0.7 * hours
    else:
        fee = 0.7 * 3 + 2.5 * (hours - 3)
    print("%.2f" % fee)
elif type == 2:
    if hours < 3:
        fee = 1.5 * hours
    else:
        fee = 1.5 * 3 + 2 * (hours - 3)
    print("%.2f" % fee)
elif type == 3:
    if hours < 2:
        fee = 2.5 * hours
    else:
        fee = 2.5 * 2 + 3.25 * (hours - 2)
    print("%.2f" % fee)
else:
    print("Invalid index")