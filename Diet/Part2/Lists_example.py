
#Define a list

c = [-10,0,6,777,-18]

print(c)

print (len(c))
#[-10, 0, 6, 777, -18]

# value of first element
print (c[0])
#-10
print (c[2])
#6

# print length
print("length of this list is = ", len(c))
#length of this list is =  5

print ("Last element of list ", c[-1])
#Last element of list  -18

a = 1
b =2

print (c[a+b])

# Lists are mutable. Assign new value ot existing element

c[4] = 17

print("Mutated List :", c)
#Mutated List : [-10, 0, 6, 777, 17]

s='hello'
# all seq can be done element by elemnt as shown above.
print(s[0])

# But Strings are immutable
# s[0]='h'

# /Library/Frameworks/Python.framework/Versions/3.6/bin/python3 /Users/amitkumar/Documents/LearningPython/python/Diet/Part2/Lists_example.py
# Traceback (most recent call last):
#   File "/Users/amitkumar/Documents/LearningPython/python/Diet/Part2/Lists_example.py", line 39, in <module>
#     s[0]='h'
# TypeError: 'str' object does not support item assignment

print (c[0] + c[1]+c[2])


a_list = []
for number in range(1,6):
    a_list += [number]
    # here A_list is a list
    # the RHS too must either be a list or any other iterable python type
print (a_list)

letters = []
letters += 'Python'
print (letters)

# for Lists, + operator acts as concatenation operator

list1 = [10,20,30]
list2 =[40,50]
concatenatesList = list1 + list2
print(concatenatesList)

# We can sue for loop also.

for i in range( len(concatenatesList)):
    print(f'{i}:{concatenatesList[i]}')

def cube_list(numbers):
    print (numbers, " ", type(numbers))
    new_list =[]
    for i in (numbers):
        print (i, " ",i**3)
        cubed= i**3
        new_list += [i**3]
    print(new_list)
    return new_list

list3 =[1,2,9,4,5]
cubed_list = cube_list(list3)
print (cubed_list)

bStr = 'Birthday'
characters=[]

for i in bStr:
    characters += [i]
print(characters)