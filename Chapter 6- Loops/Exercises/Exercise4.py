#Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.
##Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, 
##move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.
#A list of sandwiches  for a Deli.
Sandwich_orders = ['Chicken & Veggies', 'Chicken BBQ', 'Cheese & Turkey', 'Tuna', 'Meatlovers', 'Vegetarian', 'New Yorker', 'New Yorker Deluxe','Honey Toast']
#code input
finished_sandwiches = []
while Sandwich_orders:
    current_order = Sandwich_orders.pop()
    #This will allow the customer to inform the sandwich maker what type of sandwich they want to order.
    print(f"Here is your {current_order} sandwich made with the best ingredients available, Thank you for choosing our service.")
    #This will show what type of sandwiches have been prepared.
    finished_sandwiches.append(current_order)
    
    print("\nhere are the sandwiches that are made available:")
    for sandwich in finished_sandwiches:
        print(sandwich)
