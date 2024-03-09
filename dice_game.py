import random

def roll_dice():
    dice_total=random.randint(1,6)
    return dice_total
def main():
    player1=input("Enter 1st player name:\n")
    player2=input("Enter 2nd player name:\n")

    roll1=roll_dice()
    roll2=roll_dice()
    print(player1,"rolled",roll1)
    print(player2,"rolled",roll2)

    if (roll1>roll2):
        print(player1,"Wins")

    elif (roll2>roll1):
        print(player2,"Wins")

    else:
        print(player1,"and",player2,"have same number so draw")
main()