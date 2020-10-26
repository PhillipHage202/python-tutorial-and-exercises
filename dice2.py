import random
import dice

dice_two = random.randint(1,6 )
total = dice.dice_one + dice_two
print('Your total of two dices is: ' + str(total))