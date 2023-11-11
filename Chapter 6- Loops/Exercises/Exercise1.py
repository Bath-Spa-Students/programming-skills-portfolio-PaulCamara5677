## Exercise 1: Pizza Toppings :ballot_box_with_check:

#Writing a loop that allows the customer or user to add toppings onto their Pizza order until they are satisfied and enter an 'exit' value.
#print a message to assure the order will indeed have the toppings the customer or user entered.
pizza = []
#List of toppings
toppings = ('Pepperoni','Minced Chicken', 'Olives', 'Anchovies', 'Extra Cheese')
#True statement
while True:
    toppings = input("Please enter a pizza topping you wish to add on your order: ")
#The response of the code system upon the customers' request for added toppings.
    print(f"Thank you for choosing XX as your Pizza provider, The chosen {toppings} will be added to your order!")
#add_more statement to either add more toppings or to end the loop if the customer hits 'X'.
    add_more = input("Type any toppings to add more or Type X to stop:" )
#this choice will end the loop and will result in the the addition of the chosen toppings to the order.
    if add_more == "X":

        print(f"These {toppings} have been added on your Pizza order!")
        break
