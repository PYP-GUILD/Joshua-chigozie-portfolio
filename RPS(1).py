import random

def play():
    print("Welcome to Rock, Paper, Scissors!")
    options = ["rock", "paper", "scissors"]

    while True:
        user = input("Enter rock, paper, or scissors (or 'q' to quit): ").lower()
        
        if user == 'q':
            print("Thanks for playing! Goodbye.")
            break
        
        if user not in options:
            print("Invalid choice, try again.")
            continue
        
        computer = random.choice(options)
        print(f"Computer chose: {computer}")

        if user == computer:
            print("It's a tie!")
        elif (user == "rock" and computer == "scissors"):
            print("u win")
        elif (user == "scissors" and computer == "paper"):
            print("u win")
        elif (user == "paper" and computer == "rock"):
            print("You win!")
        else:
            print("You lose!")

play()