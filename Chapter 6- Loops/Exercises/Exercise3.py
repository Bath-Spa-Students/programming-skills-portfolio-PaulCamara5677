### Exercise 3: Infinity :ballot_box_with_check:
#Write a loop that never ends, and run it. (To end the loop, press ctrl-C or close the window displaying the output.)
#Infinite loop?


counter = 0
while True:
    counter +=1
    if counter % 2 == 0:
        print("Even number:", counter)
    else:
        print("Odd number:", counter)
    #This exercise will result in an ininfinite loop only stopped by either closing Video Studio code or by deleting the window in the terminal panel.