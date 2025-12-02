def play():
print("welcome to Rock, paper, scissors!")
option=["rock", "paper", "scissors"]
while True:
user=input("enter rock, paper or  scissors (or "q" to quit:").lower()
if user="q":
print("Thanks for playing!")
if user not in option:
print("invalid choice, try again.")
computer=random.choice(option)
print(f"computer chose:{computer} ")
if user==computer:
print("it's a tie!")
elif (user=="rock" and computer=="scissors"):
print("user win")
elif (user=="scissors" and computer=="paper"):
print("user wins")
elif (user=="paper" and computer=="rock"):
print("user wins")
else
print("you lose")






