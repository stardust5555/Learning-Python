# GENERAL FUNCTION
def circumferenceCircle(radius):
    return 2*3.14*radius

circumferenceCircle(2)
print(circumferenceCircle(2))


myName ='joanne'

#FUNCTION - E.G. 1
# In this example the variable myName is different when it is printed inside the function and outside the function
def printName():
    myName = 'jim'
    print('inside the function your name is', myName)

printName()
print('outside the function you name is', myName)


#FUNCTION - E.G. 2
# Redefining the global variable (now it's the same inside and outside the function)
def printName2():
    global myName
    myName = 'jim'
    print('inside the second function your name is', myName)

printName2()
print('outside the second function you name is', myName)