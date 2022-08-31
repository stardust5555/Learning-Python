str1 = [1,2,3]
str2= [4,5,6,7,8,9,10]

#Reassign
str1[0]=0

#Add number to the end
str1.append(7)

#Remove last number
str2.pop()

#Remove number
del(str1[0])
del(str2[0:2])

print(str1)
print(str2)

#List within list
yo=[['hello', 'there'],[1,2,3,4,5,6,7,8]]

result = yo[1][0]    #Gives back 1

print(result)