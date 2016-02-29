# Corey Caskey
# Section C3
# GT ID: 903120273
# Email: ccaskey6@gatech.edu
# I worked on the homework assignment alone, using only this semester's course materials.
# fluidConversion
# coneVolume
# calorieIntake
# paycheckAfterTaxes

from math import pi

def fluidConversion():
    fluidOunces = int(input("Write the number of fluid ounces that you would like to be converted"))
    gallons = int(fluidOunces / 128)
    remainGallons = (fluidOunces % 128)
    quarts = int(remainGallons / 32)
    remainQuarts = (remainGallons % 32)
    pints = int(remainQuarts / 16)
    remainPints = (remainQuarts % 16)
    gills = int(remainPints / 4)
    print(str(fluidOunces) + " fluid ounces is " + str(gallons) + " gallon(s), " + str(quarts) + " quart(s), " + str(pints) + " pint(s), and " + str(gills) + " gill(s).") 

def coneVolume():
    radius = int(input("Give the length of the radius of the cone in feet"))
    height = int(input("Give the height of the cone in feet"))
    volume = float((pi * (radius ** 2) * height) / 3)
    print("Volume of a cone with a radius of " + str(radius) + " and a height of " + str(height) + " is " + str(volume) + " feet-cubed.")
    
def calorieIntake():
    meals = int(input("Give the number of meals you've eaten"))
    miles = int(input("Give the number of miles you've run"))
    gained = meals * 500
    burned = 1600 + miles * 95
    intake = gained - burned
    print("After eating " + str(meals) + " meals and running " + str(miles) + " miles, a person gained " + str(gained) + " calories and burned " + str(burned) + " calories, leading to an intake of " + str(intake) + " calories.") 

def paycheckAfterTaxes():
    earned = float(input("Give the total money you've earned from working"))
    tax = int(input("Give the percentage of taxes taken out of your paycheck"))
    remainder = earned * ((100 - tax) / 100)
    remainder = round(remainder,2)
    print("Your corrected paycheck of $" + str(earned) + " after " + str(tax) + "% due to taxes is $" + str(remainder) + ".")
