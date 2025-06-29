import tkinter as tk
from tkinter import messagebox

"""
This python file contains my self written implementation of binary search GUI as Number Guessing Game.
This is not part of book. Rather my Experiment.
"""

class BinarySearchGame:
    def __init__(self, master, n):
        self.master = master
        self.master.title("Binary Search: Guess My Number 🤖")
        self.master.state('zoomed')
        self.low = 1
        self.high = n
        self.guess = 0
        self.guess_count = 0
        self.numbers = list(range(1, n+1))
        self.title = tk.Label(master, text="🧠 Binary Search Game", font=("Helvetica", 28, "bold"))
        self.title.pack(pady=20)
        self.label = tk.Label(master, text="Think of a number between 1 and 100.\nI'll guess it!", font=("Helvetica", 20))
        self.label.pack(pady=10)
        self.canvas = tk.Canvas(master, bg="white", height=200)
        self.canvas.pack(fill="x", padx=20, pady=20)
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=20)
        self.btn_low = tk.Button(self.button_frame, text="⬇ Too Low", font=("Helvetica", 16, "bold"),
                                 width=14, bg="#a3f7bf", activebackground="#70db98", relief="raised", command=self.too_low)
        self.btn_correct = tk.Button(self.button_frame, text="✅ Correct!", font=("Helvetica", 16, "bold"),
                                     width=14, bg="#ffe066", activebackground="#ffdd33", relief="raised", command=self.correct)
        self.btn_high = tk.Button(self.button_frame, text="⬆ Too High", font=("Helvetica", 16, "bold"),
                                  width=14, bg="#ffb3b3", activebackground="#ff8080", relief="raised", command=self.too_high)
        self.btn_low.grid(row=0, column=0, padx=10)
        self.btn_correct.grid(row=0, column=1, padx=10)
        self.btn_high.grid(row=0, column=2, padx=10)
        self.make_guess()


    def make_guess(self):
        if self.low > self.high:
            messagebox.showerror("Error", "❌ Inconsistent responses detected!")
            return -1
        self.guess = (self.low + self.high) // 2
        self.guess_count += 1
        self.label.config(text=f"🤔 Is your number **{self.guess}**?")
        if self.low != self.high:
            self.title.config(text=f"🔍 Searching between {self.low} and {self.high}...")
        else:
            self.title.config(text="")
        self.draw_numbers()


    def draw_numbers(self):
        if self.canvas.winfo_width() < 100:
            self.master.after(100, self.draw_numbers)
            return
        self.canvas.delete("all")
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        num_count = len(self.numbers)
        spacing = canvas_width / num_count
        bar_width = min(spacing * 0.8, 30)
        x_offset = (spacing - bar_width) / 2
        y1 = canvas_height * 0.25
        y2 = canvas_height * 0.75
        radius = 6
        for i, num in enumerate(self.numbers):
            x1 = i * spacing + x_offset
            x2 = x1 + bar_width
            color = "#e0e0e0"
            if self.low <= num <= self.high:
                color = "#b0dfff"
            if num == self.guess:
                color = "#ff9500"
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="", width=0)
            self.canvas.create_oval(x1, y1, x1 + radius * 2, y1 + radius * 2, fill=color, outline="")
            self.canvas.create_oval(x2 - radius * 2, y1, x2, y1 + radius * 2, fill=color, outline="")
            self.canvas.create_oval(x1, y2 - radius * 2, x1 + radius * 2, y2, fill=color, outline="")
            self.canvas.create_oval(x2 - radius * 2, y2 - radius * 2, x2, y2, fill=color, outline="")
            if num_count <= 100:
                self.canvas.create_text((x1 + x2) / 2, y2 + 12, text=str(num), font=("Helvetica", 9), anchor="n")


    def too_high(self):
        old_high = self.high
        self.high = self.guess - 1
        c = self.make_guess()
        if c == -1: self.high = old_high


    def too_low(self):
        old_low = self.low
        self.low = self.guess + 1
        c = self.make_guess()
        if c == -1 : self.low = old_low


    def correct(self):
        self.draw_numbers()
        messagebox.showinfo("🎉 Success", f"I guessed your number {self.guess} in {self.guess_count} tries!")
        self.master.quit()


root = tk.Tk()
n = 50
app = BinarySearchGame(root, n)
root.mainloop()
