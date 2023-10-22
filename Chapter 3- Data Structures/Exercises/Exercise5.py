## Exercise 5: Change Guest List :ballot_box_with_check:

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