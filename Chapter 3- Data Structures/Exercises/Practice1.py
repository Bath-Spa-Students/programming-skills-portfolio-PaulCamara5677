#Given a Python list, write a program to remove all occurrences of item 20.
#Given list:

list1 = [5, 20, 15, 20, 25, 50, 20]

#list is shown above directly taken from the practice question.

while 20 in list1:
    list1.remove(20)

print("Updated list:", list1)

#list will print out 5,  15 , 20 , 25, 50 properly.