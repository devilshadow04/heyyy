#GrabBike's pricing in Hanoi is calculated as follow: for the first 2km, the customer will be charged
#VND 12,000 and for each next km, he will be charged VND 3,500. In addition, after the first 2km, the customer
#will be charged VND 350 for each minute travel.
#Given the distance and the average speed (assume that the speed is constant), calculate the amount of money that
#the customer has to pay

distance = float(input("Enter the total distance (in km): "))
speed = float(input("Enter the speed (in km/h): "))

if distance < 0 or speed < 0:
    print ("Invalid index")
if int(distance) <= 2:
    result = 12000
else:
    result = 12000 + 3500 * (distance - 2) + 350 *  int(60 * (distance - 2)/speed)

print(result)
