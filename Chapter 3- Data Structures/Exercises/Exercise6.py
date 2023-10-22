## Exercise 6: Shrinking Guest List :ballot_box_with_check:

guests_list = ['Saher','Guinivere','Katie','Skyler']

name = guests_list[0].title()
print(f"{name}, come to my house and eat dinner with me tonight.")

name = guests_list[1].title()
print(f"{name}, come to my house and eat dinner with me tonight.")

name = guests_list[2].title()
print(f"{name}, come to my house and eat dinner with me tonight.")

name = guests_list[3].title()
print(f"{name}, come to my house and eat dinner with me tonight.")

name = guests_list[1].title()
print(f"\nSorry {name} could not make it to dinner.")

#  Guinivere could not make it to dinner! Let's invite Elise instead.
delete=(guests_list[1])
guests_list.insert(1, 'Elise')

#Resending Invitations

name = guests_list[0].title()
print(f"{name}, come to my house and eat dinner with me tonight.")

name = guests_list[1].title()
print(f"{name}, come to my house and eat dinner with me tonight.")

name = guests_list[2].title()
print(f"{name}, come to my house and eat dinner with me tonight.")

name = guests_list[3].title()
print(f"{name}, come to my house and eat dinner with me tonight.")

#The Dinner table is quite big. I should invite more people to dinner.
print("\nThe dinner table is quite big, Let'sinvite more people.")
guests_list.insert(0, 'Lyney')
guests_list.insert(2, 'Candace')
guests_list.append('MJ')

name = guests_list[0].title()
print(f"{name}, come to my house and eat dinner with me tonight.")

name = guests_list[1].title()
print(f"{name}, come to my house and eat dinner with me tonight.")

name = guests_list[2].title()
print(f"{name}, come to my house and eat dinner with me tonight.")

name = guests_list[3].title()
print(f"{name}, come to my house and eat dinner with me tonight.")

name = guests_list[4].title()
print(f"{name}, come to my house and eat dinner with me tonight.")

name = guests_list[5].title()
print(f"{name}, come to my house and eat dinner with me tonight.")

name = guests_list[6].title()
print(f"{name}, come to my house and eat dinner with me tonight.")

#The table did not arrive on time.
print("\nSorry, we can only invite two people to the dinner.")

name = guests_list.pop()
print(f"Terribly Sorry, {name.title()} but there's no more room on the table.")

name = guests_list.pop()
print(f"Terribly Sorry, {name.title()} but there's no more room on the table.")

name = guests_list.pop()
print(f"Terribly Sorry, {name.title()} but there's no more room on the table.")

name = guests_list.pop()
print(f"Terribly Sorry, {name.title()} but there's no more room on the table.")

name = guests_list.pop()
print(f"Terribly Sorry, {name.title()} but there's no more room on the table.")

#There should still be two people on the list. Let's invite them.
name = guests_list[0].title()
print(f"{name}, please come to dinner.")

name = guests_list[0].title()
print(f"{name}, please come to dinner.")

delete = (guests_list[0])
delete = (guests_list[0])

print(guests_list)