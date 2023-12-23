import random
from tkinter import *
from tkinter import messagebox

# dictionary and vars
comp_score = 0
player_score = 0

# Functions
def outcome_handler(user_choice):
    global comp_score
    global player_score
    outcomes = ["rock", "paper", "scissors"]
    random_number = random.randint(0, 2)
    print(outcomes[random_number])
    computer_choice = outcomes[random_number]
    player_choice_label.config(fg="red", text="Player Choice: " + str(user_choice))
    computer_choice_label.config(fg="red", text="Computer Choice: " + str(computer_choice))
    
    if computer_choice == user_choice:
        messagebox.showinfo("Result", "Draw")
    elif (computer_choice == "rock" and user_choice == "paper") or \
         (computer_choice == "paper" and user_choice == "scissors") or \
         (computer_choice == "scissors" and user_choice == "rock"):
        player_score += 1
        player_score_label.config(text="Player: " + str(player_score))
        messagebox.showinfo("Result", "You Win")
    else:
        comp_score += 1
        computer_score_label.config(text="Computer: " + str(comp_score))
        messagebox.showinfo("Result", "You Lose")

# Main screen
master = Tk()
master.title("SPS")

# Labels
Label(master, text="Rock, Paper, Scissors", font=("calibri", 14)).grid(row=0, sticky=N, pady=10, padx=200)
Label(master, text="Please select the option", font=("calibri", 14)).grid(row=1, sticky=N)
player_score_label = Label(master, text="Player: 0", font=("calibri", 14))
player_score_label.grid(row=2, sticky=W)
computer_score_label = Label(master, text="Computer: 0", font=("calibri", 14))
computer_score_label.grid(row=2, sticky=E)
player_choice_label = Label(master, font=("calibri", 12))
player_choice_label.grid(row=3, sticky=W)
computer_choice_label = Label(master, font=("calibri", 12))
computer_choice_label.grid(row=3, sticky=E)

# Button
Button(master, text="Rock", width=15, command=lambda: outcome_handler("rock")).grid(row=4, sticky=W, padx=5, pady=5)
Button(master, text="Paper", width=15, command=lambda: outcome_handler("paper")).grid(row=4, sticky=N, pady=5)
Button(master, text="Scissors", width=15, command=lambda: outcome_handler("scissors")).grid(row=4, sticky=E, padx=5, pady=5)

# Dummy label
Label(master).grid(row=5)
master.mainloop()
