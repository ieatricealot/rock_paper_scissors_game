import random
moves = ["rock","paper","scissor"]
question=input("do you wanan play? \n")

def show_moves(computer_move, player_choice):
    print(f"computer move is {computer_move} \nplayer move is {player_choice}")

if question == "yes":
    #print("......")
    print ("rock paper scissor")
    player_choice = input()
    computer_move = random.choice(moves)
    print(computer_move)
    if player_choice == "rock" and computer_move == "scissor":
        show_moves(computer_move,player_choice)
        print ("player win!")
    if player_choice == "scissor" and computer_move == "paper":
        show_moves(computer_move,player_choice)
        print ("player win!")
    if player_choice == "paper" and computer_move == "rock":
        show_moves(computer_move,player_choice)
        print ("player win!")
    if player_choice == computer_move:
        show_moves(computer_move,player_choice)
        print ("tie!")
    else:
        show_moves(computer_move,player_choice)
        print ("computer win!")
