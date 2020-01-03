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

diamonds = [2,3,4,5,6,7,8,9,10,11,12,13,14]
hearts = [2,3,4,5,6,7,8,9,10,11,12,13,14]
clubs = [2,3,4,5,6,7,8,9,10,11,12,13,14]
spades = [2,3,4,5,6,7,8,9,10,11,12,13,14]
suites = [diamonds, hearts, clubs, spades]


def choose_card():
    suite = random.randint(0,3)
    num = random.randint(0,12)
    if suite == 0:
        chosen_suite = "diamonds"
        card = diamonds[num]
    elif suite == 1:
        chosen_suite = "hearts"
        card = hearts[num]
    elif suite == 2:
        chosen_suite = "clubs"
        card = clubs[num]
    elif suite == 3:
        chosen_suite = "spades"
        card = spades[num]
    return [card, chosen_suite]

# result = choose_card()
# print(result[0])
# print(result[1])

def play_high_card(bet_amnt):
    p1 = choose_card()
    p2 = choose_card()
    # print(p1[0])
    # print(p1[1])
    if p1[0] == p2[0] and p1[1] == p2[1]:
        #if the cards are the same
        return f'The game is invalid the pack has illegal extras. Play again. You keep your stake {bet_amnt}.'

    elif p1[0] == p2[0]:
        if p1[1] == "spades" and p2[1] != "spades":
            #if the cards are of equal value but player one has a spade
            return f'Player one wins! {p1[0]} {p1[1]} against {p2[0]} {p2[1]}. Player one winnings are {bet_amnt}. Player two loses {bet_amnt * -1}.'
        elif p2[1] == "spades" and p1[1] != "spades":
            #if the cards are of equal value but player two has a spade
            return f'Player two wins! {p2[0]} {p2[1]} against {p1[0]} {p1[1]}. Player two winnings are {bet_amnt}. Player one loses {bet_amnt * -1}.'
        elif p1[1] == "hearts" and p2[1] == "clubs" or p1[1] == "hearts" and p2[1] == "diamonds":
            return f'Player one wins! {p1[0]} {p1[1]} against {p2[0]} {p2[1]}. Player one winnings are {bet_amnt}. Player two loses {bet_amnt * -1}.'
        elif p2[1] == "hearts" and p1[1] == "clubs" or p2[1] == "hearts" and p1[1] == "diamonds":
            return f'Player two wins! {p1[0]} {p1[1]} against {p2[0]} {p2[1]}. Player two winnings are {bet_amnt}. Player one loses {bet_amnt * -1}.'
        elif p1[1] == "clubs" and p2[1] == "diamonds":
            return f'Player one wins! {p1[0]} {p1[1]} against {p2[0]} {p2[1]}. Player one winnings are {bet_amnt}. Player two loses {bet_amnt * -1}.'
        elif p2[1] == "clubs" and p1[1] == "diamonds":
            return f'Player two wins! {p1[0]} {p1[1]} against {p2[0]} {p2[1]}. Player two winnings are {bet_amnt}. Player one loses {bet_amnt * -1}.'


    elif p1[0] > p2[0]:
        #player ones card is of higher value
        return f'Player one wins! {p1[0]} {p1[1]} against {p2[0]} {p2[1]}. Player one winnings are {bet_amnt}. Player two loses {bet_amnt * -1}.'

    elif p2[0] > p1[0]:
        #player two's card is of higher value
        return f'Player two wins! {p2[0]} {p2[1]} against {p1[0]} {p2[1]}. Player two winnings are {bet_amnt}. Player one loses {bet_amnt * -1}.'

    else:
        #logic for this scenario does not exist
        return f'Program does not have logic for this {p1[0]} {p1[1]} against {p2[0]} {p2[1]}'

# choose_card()
print(play_high_card(10))
