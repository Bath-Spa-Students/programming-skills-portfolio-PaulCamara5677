#Write a Python program that uses a while loop to find the largest number among a series of user-input values until they enter '0' to exit the loop.

largest_number = 0

#The code below will print out a loop that will put out a float value at the end.

while True:
    user_input = float (input("Please enter a number (enter '0' in order to end the loop): "))

    if user_input == 0:
        break

    largest_number = max(largest_number, user_input)

print("The Largest number shown is:", largest_number)
