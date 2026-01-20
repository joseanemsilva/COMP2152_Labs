import random

choices = ["rock", "paper", "scissors"]

playerChoice = input("Entre your choice (1=Rock, 2=Paper, 3=Scissors): ")
playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Error: choice must be between 1 and 3")
else:
    computerChoice = random.randint(1, 3)

    playerChoiceIndex = choices[playerChoice -1]
    computerChoiceIndex = choices[computerChoice -1]

    print("You chose:", playerChoice)
    print("Computer chose:", computerChoice)

    if playerChoice == computerChoice:
        print("It is a tie!")
    elif playerChoice == 0 and computerChoice == 2:
        print("Rock beats Scissor - You win!")
    elif playerChoice == 1 and computerChoice == 0:
        print("Paper beats Rock - You win!")
    elif playerChoice == 2 and computerChoice == 1:
        print("Scissor beats Paper - You win!")
    else:
        print("You lose!")