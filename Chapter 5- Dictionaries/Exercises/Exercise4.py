## Exercise 4: Rivers :ballot_box_with_check:

Rivers =  { 
    'Nile river' : 'Egypt',
 'Missisipi river' : 'USA',
 'Amazon river' : 'Brazil',
 'Amu Darya river' : 'Afghanistan' 
 }

#for allows the code to seperate the river and the country where it is located.

for River, country in Rivers.items():
    print(f'{Rivers}:\n is found in {country}')

#for loop is executed when finding key/river.
#rivers in .keys() will get each river.
for River in Rivers.keys():
    print(River)

for country in Rivers.values():
    print(country)