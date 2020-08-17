# calc grade on user input , display average

total = 0 
grade = 0 

inp = int(input("Enter the grade, -1 to exit "))

while inp != -1 :
    total += inp
    grade += 1 
    inp = int(input("Enter the grade, -1 to exit "))

print(total)
print(grade)

average = total / grade 

print ( f'average grade in 2 digits is {average:.2f}')
