bool = 1

while bool ==1:
    #Obtain dog's name, weight, and calendar Age
    dogName = input("Enter your dog's name: ")
    dogWeight = float(input("Enter your dog's weight: "))
    dogAge = float(input("enter your dog's calendar age: "))
                    
    #Use If-Else statement to calculate
    if dogAge > 2:
        if dogWeight > 90:
            dogRealAge = 21 + (dogAge - 2)*7
        elif 50 <= dogWeight <= 90:
            dogRealAge = 21 + (dogAge - 2)*6
        elif 20 <= dogWeight < 50:
            dogRealAge = 21 + (dogAge - 2)*5
        else:
            dogRealAge = 21 + (dogAge - 2)*4
    elif dogAge == 2:
        dogRealAge = 21
    else:
        dogRealAge = 15

    print(dogName, "'s dog age is ", dogRealAge, " lbs.")
    decision = input("Would you like to use the program again? (type Yes or no)")
    finalDecision = decision.lower()
    if finalDecision == "yes":
                     bool = 1
                     print("Alrighty")
    else:
                     bool = 0
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
