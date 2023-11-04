## Exercise 5: Pets :ballot_box_with_check:

Companion1 = {'Bird' : 'Ikarus' }
Companion2 = {'Cat' : 'Guinivere'}
Companion3 = {'Dog' : 'Danielle'}
Companion4 = {'Mouse' : 'Henry'}

#This list contains the "companions" and their "owners" . 
companions = [Companion1, Companion2, Companion3, Companion4]

for species in companions:
    #The secondary loop runs through a key-value pairs inside the given Dictionary


    #The key/species  will be assigned to the "companion" variable
    ##whilst the value/owner name are assigned with the "owner" value.
    for kind, owner in species.items():
        print(f'{kind} belongs to {owner}' )
        #This will print each statement for the pairs 


