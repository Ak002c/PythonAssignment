amount = int(input("enter the amount:"))
numnote = 0
rim = 0
if amount>=2000:
    numnote1 = amount//2000
    rim = amount%2000
    print(numnote1)

if rim>=500:
    numnote2 = rim//500
    rim = rim%500
    print(numnote2)

if rim>=200:
    numnote3 = rim//200
    rim = rim%200
    print(numnote3)  