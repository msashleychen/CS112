#Program Goal: program that provides guidance on whether a particular person on whether or not they should date a specific other person of a certain age

output = [15,15,15,15,15,15,15,21,21,21,21,21,21,21,25,26,26,27,27,27,28]
weight = [19,20,49,50,89,90,100,19,20,49,50,89,90,100,19,20,49,50,89,90,100]
age = [1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3]
check = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
ageList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


for i in range(0,20):
    #Ask the user for their age and the significant other's age
    dogWeight = weight[i]
    dogAge = age[i]


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
        dogRealAge = 15 + 6*(dogAge-1)

    ageList[i] = dogRealAge


    if ageList[i] == output[i]:
        check[i] = "good"
    else:
        check[i] = "bad"

print(ageList)
print(output)

print(check)

