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

# Rock, Paper, Scissors game 
while True:
    
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
        if computer_choice == rock:
            print("It's a tie!")
        elif computer_choice == paper:
            print("You lose!")
        elif computer_choice == scissors:
            print("You win!")

    # create an if statement for the user choosing paper
        
    elif user_choice == paper:
        if computer_choice == rock:
            print("You win!")
        elif computer_choice == paper:
            print("It's a tie!")
        elif computer_choice == scissors:
            print("You lose!")

    # create an if statement for the user choosing scissors

    elif user_choice == scissors:
        if computer_choice == rock:
            print("You lose!")
        elif computer_choice == paper:
            print("You win!")
        elif computer_choice == scissors:
            print("It's a tie!")

    # create an else statement for if the user inputs something other than rock, paper or scissors
        
    else:
        print("You didn't choose rock, paper or scissors.")

    # create an if statement for the user playing again 

    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != "y":
        print("Thanks for playing!")
        break
    elif play_again.lower() != "n":
        print("Let's play again!")