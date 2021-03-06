"""
Program Goal:  Your clients have several dogs. Given each dogs’ age and weight,
report (print) that dog’s age in calendar years. Finally report the average age (in dog’s years)
of all your dogs.
"""

#Declare variables outside of the while loop
bool = 1
counter = 1
total = 0

#Start loop
while bool ==1:
    #Obtain dog's name, weight, and calendar Age
    dogName = input("Enter your dog's name: ")
    dogWeight = float(input("Enter your dog's weight: "))
    dogAge = float(input("enter your dog's calendar age: "))
                    
    #Use If-Else statement to calculate
    # Case one: dog is older than 2 
    if dogAge > 2:
        #Heavy dog
        if dogWeight > 90:
            dogRealAge = 21 + (dogAge - 2)*7
        #Not-So-Heavy Dog
        elif 50 <= dogWeight <= 90:
            dogRealAge = 21 + (dogAge - 2)*6
        #Not a very heavy dog
        elif 20 <= dogWeight < 50:
            dogRealAge = 21 + (dogAge - 2)*5
        #Light dog
        else:
            dogRealAge = 21 + (dogAge - 2)*4
    #2 year old dog
    elif dogAge == 2:
        dogRealAge = 21
    #Youngest dog
    else:
        dogRealAge = 15

    #Gives the user the results
    print(dogName, "'s dog age is ", dogRealAge, " lbs.")

    #Gives the user a choice to calculate the age of another dog
    decision = input("Would you like to use the program again? (type Yes or No)")
    finalDecision = decision.lower()
    if finalDecision == "yes":
                     bool = 1
                     total += dogRealAge
                     counter += 1
                     print("Alrighty")
    else:
                     bool = 0
#Ends the program with a count and an average                     
print("You've tried this program ", counter, " times. The average of your dogs' ages is ", total/counter, "lbs.")        

#Code written by Ashley Chen

"""
INPUTS and predicted OUTPUTS
19, 1  15
20, 1  15
49, 1  15
50, 1  15
89, 1  15
90, 1  15
100,1  15

19, 2  21
20, 2  21
49, 2  21
50, 2  21
89, 2  21
90, 2  21
100,2  21

19, 3  25
20, 3  26
49, 3  26
50, 3  27
89, 3  27
90, 3  27
100,3  28
"""

