# Define an empty Tuple

student_tuple=()
print(len(student_tuple))

student_tuple = 'John', 'Grass', 4.1

print (student_tuple)
print(len(student_tuple))


another_student_tuple = 'Mary', 'Red', 4.8

print (another_student_tuple)
print(len(another_student_tuple))
# its comma that defines the tuple. Not the brackets.
single_tuple = ('red',)

print (single_tuple)
print(len(single_tuple))

# Time tuple

time_tuple = (9,16,1)
time_secs =time_tuple[0]*3600 + time_tuple[1]*60+ time_tuple[2]

tuple1 = (10,20,30)
tuple2=tuple1

print (id(tuple1) , " " , id(tuple2))
# using List inside a tuple
student_tuple = ('Amanda','Blue',[98,75,87])
student_tuple[2][1] = 85
print(student_tuple)

