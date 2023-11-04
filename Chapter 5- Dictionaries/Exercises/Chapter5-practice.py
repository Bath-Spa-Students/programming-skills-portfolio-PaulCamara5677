#To add some value in dictionary
example = {'color' : 'blue',
           'fruit' : 'blueberry',
           'place' : 'Mt. Fuji'}

#To check Dictionary type

dictionary = {'Name' : 'Paul Yram',
              'Student No.' : '19-77567',
              'Fathers Name' : 'Roderick Santiago Camara'}
print( dictionary.get ("student") )

#Next value
dictionary = {'Name' : 'Paul Yram',
              'Student No.' : '19-77567',
              'Fathers Name' : 'Roderick Santiago Camara'}
print( dictionary.get ("student","Isaac") )

#Delete method
dictionary = {'Name' : 'Paul Yram',
              'Student No.' : '19-77567',
              'Fathers Name' : 'Roderick Santiago Camara'}
del dictionary( "Student No."  ),
print(dictionary.keys()),
print(dictionary.items()),
print(dictionary.value())




