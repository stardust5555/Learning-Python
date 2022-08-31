# If you have an apostrophe inside a string you need a backslash
'he\'s a cool guy'

# Getting particular letters
greet = 'hello'
greet[0]    # first letter
greet[-1]   #last letter

# SLICING
greet[0:3]  #This includes 0 and not 3 (i.e. it gives 'hel')
greet[-1:2] #This gives us ''
greet[2:-1] #This gives us 'll'

# CONCATENATION
person = 'Niall'
greet + '' + person    #This gives 'hello Niall'

# MULTIPLICATION
greet*3     #This gives 'hellohellohello'

# STRING METHODS
greet.upper()   #Uppercase 'HELLO'
greet = greet.upper()   #Reassigns greet

cheeses = "brie, cheddar, stilton"
cheeses.split(',')  #Splits the cheeses and puts them into elements in a list

len(greet)  #Length of string

# FORMATTING (like the backticks in Javascript)
num1 = 3.14138694618
num2 = 10.237582395

#Previously we'd write
print('num1 is', num1, 'and num2 is', num2)

# Instead we can write
print ('num1 is {0} and num2 is {1}'.format(num1,num2)) 

#To get only 3 digits of each number write 
print ('num1 is {0:.3} and num2 is {1:.3}'.format(num1,num2)) 

#To get only 3 dp of each number write (f is for floating point numbers)
print ('num1 is {0:.3f} and num2 is {1:.3f}'.format(num1,num2)) 

#OR we could use F-STRINGS
print (f'num1 is {num1:.3} and num2 is {num2}') 