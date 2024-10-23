#Question 1
#Temperature  Classifier: Using a function, write a python script that takes temperature as input and classifies it into the 
#following categories:
#below 0degrees celcius: freezing
#0 to 10 degrees celcius:cold
#11 to 20 degrees celcius: noderate
#21 to 30 degrees celcius: warm
#Above 30 degrees celcius: hot

def temperature_classifier():
    temperature=float(input("Enter the temperature value in degrees celcius: "))
    classification=temperature_classifier(temperature) 
    print(f"The temperature is classified as {temperature}")
    if temperature<0 :
        print("Freezing")
    elif temperature>=0 and temperature <=10:
        print("Cold")
    elif temperature>=11 and temperature <=20:
        print("Moderate")
    elif temperature>=21 and temperature <=30:
        print("Warm")
    else:
        print("Hot")

import math
pie= math.pi
# Question 1(ii)
# The volume of a sphere with radius r is (4/3)*pie*r**2.What is the volume of the sphere with radius 8.
# Use a function and make sure the radius is entered from the keyboardand provide the answer in 1 decimal place.
def volume_of_the_sphere():

    r=float(input("Enter radius of the sphere : "))
    volume_the_sphere=(4/3)*pie*r**2
    print(f" The volume of the sphere of radius 8 is {volume_of_the_sphere:.3f}")
