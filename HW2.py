# Corey Caskey
# Section C3
# GT ID: 903120273
# ccaskey6@gatech.edu
# I worked on the homework assignment alone, using only this semester's course materials.
# cocaCola
# parksAndRec
# iLoveFrozen
# oscars
# springBreakCalc
# breakfastPlatters

def cocaCola():
    bottles = int(input("How many cans of Coke have you bought this week?"))
    totalAmount = bottles * 0.99
    return totalAmount

def parksAndRec():
    weeks = int(input("How many weeks can you watch Parks and Recreation?"))
    dailyHours = float(input("How many hours of TV do you watch per day?"))
    hoursOfTV = weeks * 7 * dailyHours
    numOfEpisodes = (hoursOfTV * 60) / 21
    return int(numOfEpisodes)
   
def iLoveFrozen(dollars):
    theater = input("Are you going to Regal, AMC, or SMG to watch the movie?")    
    if theater == "Regal":
        times = int(dollars / 12)
        print("You can see Frozen " + str(times) + " time(s).")
    elif theater == "AMC":
        times = int(dollars / 15)
        print("You can see Frozen " + str(times) + " time(s).")
    else:
        times = int(dollars / 9)
        print("You can see Frozen " + str(times) + " time(s).")
        
def oscars(winners):
    speeches = int(input("How long, in minutes, do you think each speech will be?"))
    length = winners * speeches
    hours = int(length / 60)
    timeHours = hours + 8
    minutes = length % 60
    if timeHours >= 12:
        print("The Oscars cannot go past 11:59 pm.")
    else:
       if minutes >= 0 and minutes <= 9:
          minutes = "0" + str(minutes)
          print("The oscars will end at " + str(timeHours) + ":" + minutes + " pm.")
       else: 
          minutes = minutes
          print("The oscars will end at " + str(timeHours) + ":" + str(minutes) + " pm.")

def springBreakCalc(people, miles, costOfHotel):
    mpg = int(input("What's your car's MPG?"))
    gas = float(input("What's the cost of gas?"))
    tip = int(input("What percentage tip do you want to leave?"))
    gasMoney = float((miles / mpg) * gas)
    tipMoney = float(costOfHotel * (tip / 100))
    totalCost = gasMoney + costOfHotel + tipMoney
    costPerPerson = totalCost / 3
    costPerPerson = round(costPerPerson, 2)
    print("Each person needs to pay $" + str(costPerPerson) + " this Spring Break.")

def breakfastPlatters(eggs,bacon,grits):
    eggPlatters = int(eggs / 2)
    baconPlatters = int(bacon / 3)
    gritsPlatters = int(grits / 1)
    if eggPlatters <= baconPlatters and eggPlatters <= gritsPlatters:
        numOfPlatters = eggPlatters
    elif baconPlatters <= eggPlatters and baconPlatters = gritsPlatters:
        numOfPlatters = baconPlatters
    else:
        numOfPlatters = gritsPlatters
    return numOfPlatters