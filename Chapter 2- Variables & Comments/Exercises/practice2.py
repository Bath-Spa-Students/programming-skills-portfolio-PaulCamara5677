#Q2:Write a python program that takes courses marks as input and then calculates average of all the
#courses. After calculating the average, calculate the percentage of a student using total marks. Assume
#the total of all the courses marks is 500 or take the total marks from the user as input. 

course1 = float(input("Course 1 marks: "))
course2 = float(input("Course 2 marks: "))

#The two variables above will show the value of each course marks.

#whilst the code below will show the formula of the total of both marks divided by 5 in order to see a student's average marks.

average_marks = ( course1 + course2 ) / 5

percentage = float(input("Enter the total of both marks: "))

#The ones below will print out the total average_marks of the courses and the total average of the student's marks.

print(f"The average for both courses is: {average_marks:.2f}")
print(f"The percentile average of the student is: {percentage:.2f}%")