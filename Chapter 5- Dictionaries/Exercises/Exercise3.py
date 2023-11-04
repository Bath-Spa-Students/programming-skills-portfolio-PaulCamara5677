#Glossary loop of keywords and their definition

Glossary = {'Variable': 'Python variables contains the value of the stored data.',
            'Tuple' : 'Python tuples are a type of data structure that is very similar to lists.',
            'Operator' : 'An operator in Python is used to define variables, functions, and classes.',
            'Repository' : 'Python repositories are where software development teams that develop Python share their code artifacts.',
            'Commit' : 'This method lets an operator save all the changes made in a database.'
            }

#The contents above  are keywords in Code Lab subject and their definition.

for word, definition in Glossary.items():
    print(f'{word}:\n {definition}')
    #this will execute the print statement each pair the operator will find.
    ##using f strings can organize each of the keyword and their meanings.