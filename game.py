# ------------Rock,Paper,scissor Game--------------------

"""
WORKFLOW OF PROJECT:
1-Input from user(rock,paper,scissor)
2-Computer choice(computer will randomly not conditionally)
3-Result print

CASE:
A - Rock
rock -rock = tie
rock - paper = paper win
rock - scissor = rock win


B - paper
paper - paper = tie
paper - scissor = scissor win
paper - rock = rock win

C- scissor
scissor - scissor = tie
scissor - paper = scissor win
scissor - rock = rock win
"""

# ------------------Game code------------

# import random for choice any random values
import random
item_list = ["rock","paper","scissor"]
user_choice = input("enter your move= rock,paper,scissor=  ")
comp_choice =random.choice(item_list)

print(f"user_choice= {user_choice},comp_choice= {comp_choice}")

# condition 
if user_choice ==  comp_choice:
    print("both are same = match tie")

elif user_choice == "rock":
    if comp_choice == "paper":
        print("paper covered rock, computer win ")
    else:
        print("rock smashes scissor, you win ")

elif user_choice == "paper":
    if comp_choice == "scissor":
        print("scissor cut the paper, computer win ")
    else:
        print("paper covers rock, you win ")

elif user_choice == "scissor":
    if comp_choice == "paper":
        print("scissor cut the paper,you win ")
    else:
        print("rock smashes scissor,you win ")
    
# -----------------end-----------------------------------------


