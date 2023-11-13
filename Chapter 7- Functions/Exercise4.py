def make_shirt(size = 'Large', message= 'Certified Python enjoyer'):
#function will define the size and message that will be the shirt's value.
    print(f'size: {size.title()}, Message: {message}')
#print will display the details from the make_shirt size and message input below   
    make_shirt()
    make_shirt(size= 'medium')
    make_shirt(size='small', message='Certified Python Gang')
