num = [1,2,3,4,5]

for nu in num :
    if nu == 4:
        print('found')              #break  method
        break
    print(nu)

for nu in num :
    if nu == 4:
        print('found')
        continue                   #continue method
    print(nu)

for nu in num :
    for letter in ['a', 'b','c','abc']:
        # if letter == ['c']:
        #     break
        print(nu, letter)