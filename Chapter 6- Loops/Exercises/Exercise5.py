## Exercise 5: No Pastrami :ballot_box_with_check:

#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code 
##near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all
###occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['Subway Special', 'Chicken & Cheese', 'Meatball Sub', 'Sausage club']
print("Apologies, but we do not have any ingredients to make a Pastrami sandwich at the moment.")
while "Subway Special" in sandwich_orders:
    sandwich_orders.remove('Subway Special')
finished_sandwiches = []
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"The {current_order} sandwich order is being prepared...")
    finished_sandwiches.append(current_order)
print("\nAll sandwiches have been prepared:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
