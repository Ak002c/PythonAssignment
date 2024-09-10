total =0
product = 1
i=0

while user != 'q':
    user = input("enter a number or press q for quit:")
    if user == 'q':
        break
    else:
        total += user
        product *= user
    i +=1

print(total,'/n',product)        