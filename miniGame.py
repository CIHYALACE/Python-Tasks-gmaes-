import random

def getChoices():
    options = ["Rock", "Paper", "Scissor"]
    playerChoice = input("Enter A choice (Rock , Paper , scissor): ").capitalize()
    computerChoice = random.choice(options)
    choices = {"player": playerChoice, "computer": computerChoice}
    return choices

choices = getChoices()

player = choices["player"]
computer = choices["computer"]

def winnerDesider(player , computer):
    if(player == computer):
        print(f"You Chose {player} & The Computer Chose {computer}")
        print("It Is A Tie!")

    elif(player == "Rock"):
        if(computer == "Paper"):
            print(f"You Chose {player} & The Computer Chose {computer}")
            print ("Rock Coverd By Paper , You Lose!")
        else:
            print(f"You Chose {player} & The Computer Chose {computer}")
            print ("Rock Broke The Scissor , You Win!")

    elif(player == "Paper"):
        if(computer == "Rock"):
            print(f"You Chose {player} & The Computer Chose {computer}")
            print ("Rock Coverd By Paper , You Win!")
        else:
            print(f"You Chose {player} & The Computer Chose {computer}")
            print ("Scissor Cut Paper , You Lose!")

    elif(player == "Scissor"):
        if(computer == "Paper"):
            print(f"You Chose {player} & The Computer Chose {computer}")
            print ("Scissor Cut Paper , You Win!")
        else:
            print(f"You Chose {player} & The Computer Chose {computer}")
            print ("Rock Broke The Scissor , You Lose!")


winnerDesider(player, computer)
        