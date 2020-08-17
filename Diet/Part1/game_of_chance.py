import random
# roll two six sided dice
def roll_a_dice():
    dice_1 = random.randrange(1, 7)
    dice_2 = random.randrange(1, 7)
    return dice_1, dice_2

dice_1 = dice_2 = 0


dice_1,dice_2 = roll_a_dice()

game = ""
point=0
print ("dice_1=", dice_1, "dice_2", dice_2)

sum = dice_1 + dice_2
if ( sum == 7 or sum == 11):
    print("Player Wins")
    game = "ends"
elif ( sum == 2 or sum == 3 or sum ==12 ):
    print("Player Loses")
    game = "ends"
elif ( sum == 4 or sum == 5 or sum ==6 or sum == 8 or sum == 9 or sum == 10):
    point = sum
    game = "continue"
print ("point = ",point)
while ( game == "continue"):
    dice_1,dice_2 = roll_a_dice()
    sum_inner = dice_1 + dice_2
    print("sum in inner loop " , sum_inner)
    if (sum_inner == 7) :
        print("Player Loses")
        break
    elif sum_inner == point :
        print("Player Wins")
        break
    else:
        continue



