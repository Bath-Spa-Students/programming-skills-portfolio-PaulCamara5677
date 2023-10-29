Income = int(input('Enter your income per year: '))
work_experience = float (input('Enter your work experience: '))

if Income > 100000:
      if work_experience >=6:
           print('You are eligible for this loan')
      else:
         print ('Sorry your work experience is less than 6 years ')
else :
         print ('Your income is less than 120000')

