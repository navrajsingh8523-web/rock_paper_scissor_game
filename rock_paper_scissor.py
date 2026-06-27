import tkinter as tk
import random

def game(user):
    options = ["Rock", "Paper", "Scissors"]
    computer = random.choice(options)

    if user == computer:
        result = "Tie"
    elif user == "Rock" and computer == "Scissors":
        result = "You Win"
    elif user == "Paper" and computer == "Rock":
        result = "You Win"
    elif user == "Scissors" and computer == "Paper":
        result = "You Win"
    else:
        result = "Computer Wins"

    label.config(text="You: " + user +
                      "\nComputer: " + computer +
                      "\nResult: " + result)

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x200")

btn1 = tk.Button(root, text="Rock", command=lambda: game("Rock"))
btn1.pack()

btn2 = tk.Button(root, text="Paper", command=lambda: game("Paper"))
btn2.pack()

btn3 = tk.Button(root, text="Scissors", command=lambda: game("Scissors"))
btn3.pack()

label = tk.Label(root, text="Choose an option")
label.pack()

root.mainloop()