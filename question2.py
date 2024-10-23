# Question 2
# Define a function named calculate_bmi that takes a person's weight (in kilograms) and height in (meters) as parameters and returns their BMI . (BMI= weight/height)
# Calculate and send their BMI category:
# Below 18.5: "Underweight"
# 18.5 to 24.9: "Normal weight"
# 25 to 29.9: "Overweight"
# 30 or above: "Obese"
def calculate_bmi ():
    weight=float(input("Enter a person's weight in kgs: "))
    height=float(input("Enter a person's height in meters: "))
    BMI=weight/height
    print("BMI")
    if BMI < 18.5 :
        print("Underweight")
    elif 18.5<= BMI <=24.9:
        print("Normal weight")
    elif 25 <= BMI <=29.9:
        print("Overweight")
    else:
        print("Obese")

 
 

#   Question 2(ii)
# Use a function to calculate the volume of a cylinder v= pie*r**2*h. Choose a function name in line with what you want to achieve.Radius r and height h should be in parameters. Make sure you use the real pie value (import math).
import math
pie=math.pi
def calculate_the_volume_of_a_cylinder ():
    r=float(input("Enter radius of the cylinder in meters:"))
    h=float(input("Enter the height of the cylinder in meters: "))
    volume_of_the_cylinder=pie*r**2*h
    print("volume of the cylinder")
