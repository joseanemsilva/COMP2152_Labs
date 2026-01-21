import random

choices = ["rock", "paper", "scissors"]
playerScore = 0
computerScore = 0

for _round in range(5):
    playerChoice = input("Enter your choice (1=Rock, 2=Paper, 3=Scissors): ")
    playerChoice = int(playerChoice)

    if playerChoice < 1 or playerChoice > 3:
        print("Error: choice must be between 1 and 3")
    else:
        computerChoice = random.randint(1, 3)

        playerChoiceName = choices[playerChoice -1]
        computerChoiceName = choices[computerChoice -1]

        print(f"You chose: {playerChoiceName}")
        print(f"Computer chose: {computerChoiceName}")

        if playerChoice == computerChoice:
            print("It is a tie!")
        elif playerChoice == 0 and computerChoice == 2:
            print("Rock beats Scissor - You win!")
            playerScore += 1
        elif playerChoice == 1 and computerChoice == 0:
            print("Paper beats Rock - You win!")
            playerScore += 1
        elif playerChoice == 2 and computerChoice == 1:
            print("Scissor beats Paper - You win!")
            playerScore += 1
        else:
            print("You loose!")
            computerScore += 1

print(f"Player Score: {playerScore}")
print(f"Computer Score: {computerScore}")