# IF STATEMENTS
age = int(input('Enter your age'))

if age<10:
    print('You are so cool')
elif age<=40: 
    print('You are still young')
else:
    print('You\'re getting on bro')


vege = input('are you a vegetarian (y/n')
if vege == 'y':
    print('Here is some risotto')
else:
    print('Here is some chicken')

# FOR LOOPS
colours = ['black', 'brown', 'green', 'pink']

for i in colours:
    print(i)

for colour in colours:
    if colour == 'pink':
        print(f'{colour} - This is the best colour')
    else:
        print(colour)

    #Break out of the loop
    numbers = [1,2,3,4]

    for number in numbers:
        if number == 3:
            print(f'{number} - This is my fav number')
            break
        else:
            print(number)

# WHILE LOOP
age = 12
num = 0

while num <age:
    if num <age:
        print(num)
        num+=1

while num <age:
    #If we don't want to display the number 0
    if num == 0:
        num+=1  #prevents infinite loop
        continue    #tells the code to go back to the start of the while loop and carry on
    #If the number is even print it
    if num %2==0:
        print(num)
    #If number is greater than 10 break the chain
    if num >10:
        break
    #Keep adding one to the number
    num+=1

# RANGE
for n in range(10):
    print(n)

for n in range (0,20,3):
    print(n)

    #Going backwards through a list
    food = ['burger', 'sandwich', 'pizza', 'pineapple']

    for n in range(len(food)-1, -1, -1):
        print(n, food[n])
 