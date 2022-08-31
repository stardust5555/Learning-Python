# We can as the user to input some data in the command line
print('Hello. Enter your name:')
name = input()
print("Hey there, " + name)


#Area of circle
radius = input('Enter the radius of your circle:')
area= 3.1415 * int(radius)**2   #int(radius) turns the users input from a string to an integer
print('The area of your circle is:', area)
