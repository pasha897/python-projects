import random

options = ("rock","paper","scissor")
running = True
while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice: ")

    print(player)
    print(computer)

    if player == computer:
        print("its tie")
    elif (player == "rock" and computer == "scissor") or (player == "scissor" and computer == "paper") or (player == "paper" and computer == "rock"):
        print("you win")
    else:
        print("you lose")

    if not input("play again(y): ").lower() == 'y':
        running = False
