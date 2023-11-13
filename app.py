#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import random

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")


# create rock, paper and scissors variables
rock = "rock"  
paper = "paper"
scissors = "scissors"

# create a variable for the user's choice
user_choice = input("Do you choose rock, paper or scissors? ")

# each time the user plays again, the computer's choice should be random
# create a variable for the computer's choice
computer_choice = random.randint(0, 2)
if computer_choice == 0:
    computer_choice = "rock"
elif computer_choice == 1:
    computer_choice = "paper"
else:
    computer_choice = "scissors"
print("The computer chose " + computer_choice + ".")


# create an if statement for the user choosing rock

if user_choice == rock:
    if computer_choice == 0:
        print("It's a tie!")
    elif computer_choice == 1:
        print("You lose!")
    elif computer_choice == 2:
        print("You win!")

# create an if statement for the user choosing paper
    
    elif user_choice == paper:
        if computer_choice == 0:
            print("You win!")
        elif computer_choice == 1:
            print("It's a tie!")
        elif computer_choice == 2:
            print("You lose!")

# create an if statement for the user choosing scissors

    elif user_choice == scissors:
        if computer_choice == 0:
            print("You lose!")
        elif computer_choice == 1:
            print("You win!")
        elif computer_choice == 2:
            print("It's a tie!")

# create an else statement for if the user inputs something other than rock, paper or scissors
    
        else:
            print("You didn't choose rock, paper or scissors. Try again.")

# create an if statement for the user playing again 

play_again = input("Do you want to play again? (y/n) ")
if play_again == "y":
    user_choice = input("Do you choose rock, paper or scissors? ")
    computer_choice = "rock"
elif play_again == "n":
    print("Thanks for playing!")
else:
    print("You didn't type y or n. Try again.")


