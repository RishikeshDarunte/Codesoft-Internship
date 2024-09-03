import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        
        self.user_score = 0
        self.computer_score = 0
        
        self.instructions_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Helvetica", 14))
        self.instructions_label.pack(pady=10)
        
        self.result_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)
        
        self.score_label = tk.Label(root, text="User Score: 0 | Computer Score: 0", font=("Helvetica", 12))
        self.score_label.pack(pady=10)
        
        self.rock_button = tk.Button(root, text="Rock", command=lambda: self.play("rock"), width=10)
        self.rock_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.play("paper"), width=10)
        self.paper_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.play("scissors"), width=10)
        self.scissors_button.pack(side=tk.LEFT, padx=10, pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(["rock", "paper", "scissors"])
        result = self.determine_winner(user_choice, computer_choice)
        self.update_score(result)
        self.display_result(user_choice, computer_choice, result)

    def determine_winner(self, user, computer):
        if user == computer:
            return "It's a tie!"
        elif (user == "rock" and computer == "scissors") or \
             (user == "scissors" and computer == "paper") or \
             (user == "paper" and computer == "rock"):
            return "You win!"
        else:
            return "You lose!"

    def update_score(self, result):
        if result == "You win!":
            self.user_score += 1
        elif result == "You lose!":
            self.computer_score += 1
        self.score_label.config(text=f"User Score: {self.user_score} | Computer Score: {self.computer_score}")

    def display_result(self, user_choice, computer_choice, result):
        self.result_label.config(text=f"You chose: {user_choice}, Computer chose: {computer_choice}. {result}")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
