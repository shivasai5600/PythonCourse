names = 'sai'

if names == 'sai':
    print(f'my name is : {names}')              #if - else statement
else:
    print('it\'s not my name')

if names == 'sa':
    print(f'my name is : {names}')
else:
    print('it\'s not my name')


if names == 'si':
    print(f'my name is : {names}')                #if - elif -  else statement
elif names == 'sai':
    print(f'my name is : {names}')
else:
    print('it\'s not my name')

                                       # """ and, or , not"""
name = 'kohli'
name2 = 'virat'
if name and name2==False:            #and
    print(f'{name2} {name}')
else:
    print('not a nam' )

if name or name2:                     #or
    print(f'{name2} {name}')
else:
    print('not a nam' )

if not name2==False:                  #not
    print(f'{name2} {name}')
else:
    print('not a nam' )

cv = '',{}, None, [], False
if cv is True:
    print('zsd')