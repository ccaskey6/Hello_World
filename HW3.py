# Corey Caskey
# Section C3
# GT ID: 903120273
# Email: ccaskey6@gatech.edu
# I worked on this homework assignment alone,
# and referred to http://www.tutorialspoint.com/python/string_center.htm
# mixtapeFire
# myFaveSong
# illuminatiConfirmed
# decrementNumber
# numberTie
# countUp

def mixtapeFire(timesPlayed,rating):
    if rating > 5:
        return "Invalid input. Try again."
    elif timesPlayed >= 1000 and rating >= 3:
        return "Your mix tape is fire!"
    elif timesPlayed < 1000 or rating < 3:
        return "You should quit the rap game."

def myFaveSong(song,artist):
    music = input("Guess my favorite song")
    counter = 1
    guess = 1
    hint = 0  
    while counter < 5: 
        if guess == 1:
            if music == "hint" or music == "Hint" or music == "HINT":
                print("The artist who wrote the song is: " + str(artist))
                music = input("Guess my favorite song")
                hint = hint + 1
            if music.lower() != song.lower():
                music1 = input("Try again. Guess my favorite song")
                guess = guess + 1
                counter = counter + 1
            else:
                counter = 5
        else:
            if music1 == "hint" or music1 == "Hint" or music1 == "HINT":
                print("The artist who wrote the song is: " + str(artist))
                music1 = input("Try again. Guess my favorite song")
                hint = hint + 1
            if music1.lower() != song.lower():
                music1 = input("Try again. Guess my favorite song")
                guess = guess + 1
                counter = counter + 1
            else:
                counter = 5      
    if guess == 5:
        print("You have exceeded the number of tries.")
    else:
        print("Great Job! It took you " + str(guess) + " tries and " + str(hint) + " hints to guess my favorite song.")  
    print("Thank you for playing!") 

def illuminatiConfirmed(secretMsg):
    newStr = ""
    count = 0
    for letter in secretMsg:
        if letter == "$":
            count = count + 1
    if count == 3:
        for i in secretMsg:
            secretMsg = secretMsg.replace("$","s")
            newStr = newStr + secretMsg
            print(newStr)
            print("Illuminati Confirmed.")
            break
    else:
        print(secretMsg)
        print("Probably not Illuminati.") 

def decrementNumber(aString):
    guess = input("Enter a single positive integer")
    newString = ""
    for value in aString:
        if value == guess:
            guess = int(guess) - 1
            aString = aString.replace(value, str(guess))
            newString = newString + aString
            return newString
        if guess not in aString:
            return "Try a different number"
            
def numberTie(num):
    for number in range(num-1,0,-1):
        line = str(number)*(number*2)
        print(line.center((num*2)," "))
    for number2 in range(1,num+1,1):
        line2 = str(number2)*(number2*2)
        print(line2.center((num*2)," "))
    for number3 in range(num,0,-1):
        line3 = str(number3)*(number3*2)
        print(line3.center((num*2)," "))

def countUp(start,limit,increment):
    newStr = ""
    for num in range(start,limit+1,increment):
        newStr = newStr + str(num) + ","
    newerStr = newStr[:-1] + ""
    print(newerStr)
               