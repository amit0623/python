magicians = ['amit','karl','pench']

# Try to make the list of variable name as plural
# Try to make the variable name in for loop as singular

for magician in magicians:
    print(magician)

for number in range ( 1,8):
    print (number)

#If you want to make a list of numbers, you can convert the results of range() directly into a list using the list() function.

numbers = list(range(1,11))
print(numbers)

# generate a list of square of num

square = []
for number in range ( 1, 11 ) :
    square.append(number ** 2 )
print(square)

# Few stats functions of lists

digits = list(range(1,12))
print(min(digits))
print(max(digits))
print(sum(digits))

# List Compre

squares = [number ** 2 for number in range (1,12 )]
print(squares)

# working with slices

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print (players[0:3])
# To generate 2,3,4 items of this list
print(players[1:4])
# if you omit the first index of this slice, then default index == 0

print(players[:3])

# if you want all elements from position 2 to end of list
#then omit the last index

print(players[2:])

for player in players[:3]:
    print(player)

# Copying a list
# To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ([:]).
# This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.

my_foods = ['mango','apple','roti','rice']
# Note how slicing produces a new list
friends_food = my_foods[:]


print(my_foods)
print(friends_food)
my_foods.append('guava')
friends_food.append('pizza')

print(my_foods)
print(friends_food)

# Working with Tples

dimensions = (10,20)
print(dimensions[0])
print(dimensions[1])

dimensions = (30,4)
print(dimensions[0])
print(dimensions[1])
