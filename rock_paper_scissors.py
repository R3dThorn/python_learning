from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

player = False
while player == False:
    player = input("Rock, Paper, Scissors!")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("Too Bad!", computer, "covers", player, ".")
        else:
            print("You win!", player, "smashes", computer, ".")
    elif player == "Paper":
        if computer == "Scissors":
            print("Too Bad!", computer, "cuts", player, ".")
        else:
            print("You win!", player, "covers", computer, ".")
    elif player == "Scissors":
        if computer == "Rock":
            print("Too Bad!", computer, "smashes", player, ".")
        else:
            print("You win!", player, "cuts", computer, ".")
    else:
        print("That's not valid. Check your spelling and try again.")
    player = False
    computer = t[randint(0,2)]