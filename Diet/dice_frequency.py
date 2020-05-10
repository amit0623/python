# calc frequence that when a die is rolled 6 Million times, how may times does each face occur.


import random

frequency_1 = 0 
frequency_2 = 0 
frequency_3 = 0 
frequency_4 = 0 
frequency_5 = 0 
frequency_6 = 0 


for roll in range (6000000):
    value = random.randrange(1,7)
    
    if value == 1 : 
        frequency_1 += 1 
    if value == 2 : 
        frequency_2 += 1     
    if value == 3 : 
        frequency_3 += 1 
    if value == 4 : 
        frequency_4 += 1      
    if value == 5 : 
        frequency_5 += 1 
    if value == 6 : 
        frequency_6 += 1 

print("Dice    Frequency")
print("1",frequency_1)
print("2",frequency_2)
print("3",frequency_3)
print("4",frequency_4)
print("5",frequency_5)
print("6",frequency_6)

# Formattd String 

print(f'Face{"Frequency":>13}')
print(f'{1:>4}{frequency_1:>13}')
print(f'{2:>4}{frequency_2:>13}')
print(f'{3:>4}{frequency_3:>13}')
print(f'{4:>4}{frequency_4:>13}')
print(f'{5:>4}{frequency_5:>13}')
print(f'{6:>4}{frequency_6:>13}')
