import random

money = 100
num = random.randint(1, 10)

def coin_toss():
    if num <= 5:
        return "Heads"
    elif num > 5 and num <= 10:
        return "Tails"

def play_heads_or_tails_bet(bet_amnt, choice):
    result = coin_toss()
    if result == choice:
        return f'You chose {result}. Congratulations you have won {bet_amnt}.'
    elif result != choice:
        return f'You chose {result}. Bad luck you have lost -{bet_amnt}.'

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum = dice1 + dice2
    if sum % 2 == 0:
        return "Even"
    elif sum % 2 > 0:
        return "Odd"

def play_cho_han_bet(bet_amnt, choice):
    result = roll_dice()
    if result == choice:
        return f'You chose {choice}. Congratulations you have won {bet_amnt}.'
    elif result != choice:
        return f'You chose {choice}. Bad luck you have lost -{bet_amnt}.'

print(play_heads_or_tails_bet(10, "Heads"))
print(play_cho_han_bet(10, "Odd"))
