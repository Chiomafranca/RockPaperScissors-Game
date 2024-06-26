import random

options = ("rock", "paper", "scissors")

running = True


while running:
    

    computer = random.choice(options)
    player = None

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you  win!")
    elif player == "paper"  and computer == "rock":
        print("you  win!")
    elif player == "scissors" and computer == "paper":
        print("you win!")   
    else:
        print("you lose!")  
    play_again = input("play again? (y/n): ").lower()
    if not play_again == "y":
        running = False
print("Thanks for playing")