"""
Code created by Ashley Chen
Programming Goal: Have the user enter a name that may be in the list. If it is, the program will tell the user 
what the name's index is.
"""

def intro(): #Intro to the program
	print("You have a list of names. The user wants to find out if a particular name is on the list and, 
	if so, where (at what positions)")

def user(name): #User enters info for the program
	name = input("Enter the name you would like to find in the list: ")
	return name

def find(name):
	correct = 0 #0 when the name is not found. 1 when found.
	listt = ['Trey', 'mary', 'Ashley', 'Drew', 'Candice', 'Casey']
	for guess in range (0,len(listt)):
		if listt[guess] == name: #When it's found
			print("\n" + name + " is found in the list. It is under index number " + str(guess))
			guess = len(listt)
			correct = 1
	if correct == 0: #When it's not found
		print("\n" + "Sorry. The name, " + name + " was not found in the list.")

def main(): #Simple Program
	name = ''
	intro()
	name = user(name)
	find(name)

game = 'y' #Actual program with a loop
while game == 'y':
	main()
	game = input("\n" + "Try again? Enter y to continue and n to quit: ")
	print("\n")
print("Goodbye")
