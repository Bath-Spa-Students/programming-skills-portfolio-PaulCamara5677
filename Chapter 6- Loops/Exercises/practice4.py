#Write a Python program that uses the break statement to exit a for loop when a specific condition is met.
people = ['Peter','Evelyn','Thomas','Claire']
for person in people:
    if person == 'Thomas':
        print(f"{person} has been Accepted.")
        break
    print(f"{person} is currently awaiting Acceptance...")

print("conditions have been met and task is Completed.")