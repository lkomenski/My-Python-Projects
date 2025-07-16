import tkinter as tk
from tkinter import messagebox
import hangman_logic as logic

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("600x600")
        self.master.resizable(False, False)

        self.wins = 0
        self.losses = 0

        self.setup_widgets()
        self.reset_game()

    def setup_widgets(self):
        self.title_label = tk.Label(self.master, text="🎉 Welcome to Hangman! 🎉", font=("Arial", 18))
        self.title_label.pack(pady=10)

        self.hangman_label = tk.Label(self.master, text="", font=("Courier", 12), justify="left")
        self.hangman_label.pack()

        self.word_label = tk.Label(self.master, text="", font=("Arial", 24))
        self.word_label.pack(pady=10)

        self.guessed_label = tk.Label(self.master, text="Guessed letters: ", font=("Arial", 12))
        self.guessed_label.pack()

        self.attempts_label = tk.Label(self.master, text="", font=("Arial", 12))
        self.attempts_label.pack(pady=5)

        self.input_entry = tk.Entry(self.master, font=("Arial", 14))
        self.input_entry.pack(pady=5)

        self.submit_button = tk.Button(self.master, text="Submit Guess", command=self.submit_guess)
        self.submit_button.pack(pady=5)

        self.score_label = tk.Label(self.master, text="🏅 Score — Wins: 0 | Losses: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        self.play_again_button = tk.Button(self.master, text="🔁 Play Again", command=self.reset_game)
        self.play_again_button.pack(pady=5)

    def reset_game(self):
        self.chosen_word = logic.choose_word()
        self.word_display = ['_' for _ in self.chosen_word]
        self.attempts = 8
        self.guessed_letters = set()
        self.word_guess_used = False
        self.update_display()

    def submit_guess(self):
        guess = self.input_entry.get().lower()
        self.input_entry.delete(0, tk.END)

        if not guess.isalpha():
            messagebox.showwarning("Invalid Input", "⚠️ Please enter only letters.")
            return

        if len(guess) == 1:
            if guess in self.guessed_letters:
                messagebox.showinfo("Already Guessed", "🔁 You've already guessed that letter.")
                return

            self.guessed_letters.add(guess)

            if guess in self.chosen_word:
                for index, letter in enumerate(self.chosen_word):
                    if letter == guess:
                        self.word_display[index] = guess
            else:
                self.attempts -= 1

        elif len(guess) > 1:
            if self.word_guess_used:
                messagebox.showinfo("Full Word Guess Used", "⚠️ You've already used your one full-word guess.")
                return
            self.word_guess_used = True
            if guess == self.chosen_word:
                self.word_display = list(self.chosen_word)
            else:
                self.attempts -= 1

        self.update_display()

        if '_' not in self.word_display:
            self.wins += 1
            self.update_display()
            messagebox.showinfo("You Win!", f"🎉 You guessed the word: {''.join(self.word_display)}\n🏆 You live to see another day...for now...")
        elif self.attempts == 0:
            self.losses += 1
            self.word_display = list(self.chosen_word)
            self.update_display()
            messagebox.showinfo("Game Over", f"💀 You ran out of attempts. The word was: {self.chosen_word}\n☠️ You lost!")

    def update_display(self):
        self.hangman_label.config(text=logic.get_hangman_stage(self.attempts))
        self.word_label.config(text=' '.join(self.word_display))
        self.guessed_label.config(text="Guessed letters: " + ', '.join(sorted(self.guessed_letters)))
        self.attempts_label.config(text=f"Remaining attempts: {self.attempts}", fg=logic.color_attempts(self.attempts))
        self.score_label.config(text=f"🏅 Score — Wins: {self.wins} | Losses: {self.losses}")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
