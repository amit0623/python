
bicycle = ['hero', 'btwin', 'crash', 'zoom', 'bird']

print (bicycle)

# To access the third element

print ( bicycle[2])

# Convert to String using title method

print (bicycle[2].title())

# To print last element of the list

print ( bicycle[-1])

#Modifying Elements in a List

bicycle[0] = 'cheetah'
print (bicycle)

# use .append to add element to the last element of the list
# Append is used more commonly when the list to be built is dynamic in nature

bicycle.append('caravan')
print((bicycle))

# To insert a value at a specific location use below
bicycle.insert(0,'BMW')
print(bicycle)
#If you know the position of the item you want to remove from a list, you can use the del statement.

del bicycle[0]
print(bicycle)

#The pop() method removes the last item in a list,
# but it lets you work with that item after removing it.

popped_bicycle = bicycle.pop()

#if no argument is given the last element from the list
#is popped out by default.

print("the cycle that got popped was ", popped_bicycle)
print(bicycle)
# Put specific index if you know its position

popped_bicycle = bicycle.pop(0)

print("the cycle that got popped was ", popped_bicycle)
print(bicycle)

# If you know the value of an element then you can use the remove methods
bicycle.remove('zoom')
print(bicycle)

# bicycle.remove('zoo1m')
# print(bicycle)
# If you try to remove a value which is not present in the list
# then you will get the below error
#ValueError: list.remove(x): x not in list

# Sorting a list

cars = ['bmw','audi','toyota','subaru']
cars.sort()
print (cars)

# to sort in reverse directions
cars.sort(reverse=True)
print(cars)

# to sort only for display purpose, use the sorted function
cars = ['bmw','audi','toyota','subaru']

print("in Sorted functions ", sorted(cars))

print ("Value of cars array as of now " , cars)

# Reverse the order of a list using the reverse function
cars = ['bmw','audi','toyota','subaru']

cars.reverse()
print("cars in reverse order ",cars)

# find the lenght of list using the len function

print(len(cars))

# Example

places = ['New York', 'London','Sydney', 'California','Kerala']

print("original", places)
print(sorted(places))
print(places)
print(sorted(places,reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)

#  Safest vway is -1 to access last element
#The only time this approach will cause an error is when you request the last item from an empty list:
