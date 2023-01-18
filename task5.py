
# Using the example https://github.com/PavelMostovoy/hillel/blob/master/app_tk.py
# you need to make an application that will wait for the user to click on the button when the color of the title or button is red.
# (the color should change, from a certain number of colors, while the color is on, the color should not be constant, but should be within some reasonable limits)
# The application should count how long it took the user, from the moment the red light turned on, until the moment the button was pressed.
# This information should be displayed on the screen.
# +10 points : Add functionality that will display the number of false button presses (when a different color was on)
# This information should also be displayed on the screen.
# Information should be displayed explicitly - with inscriptions (output of just numbers without a description is considered an error)
import tkinter as tk
import random
from time import time


class TimerCalculator:

    colors = ["red", "blue", "green", "yellow"]
    timer = 0
    false_clicks = 0

    def __init__(self):

        self.window = tk.Tk()

        self.window.geometry("300x300")

        self.label = tk.Label(
            text="Timer Calculator",
            foreground="white",  # Set the text color to white
            background="black",  # Set the background color to black
            width=100,
            height=2,
        )

        self.frame = tk.Frame(height=10)

        self.button = tk.Button(
            text="Click me!",
            bg="blue",
            fg="yellow",
            width=10,
            height=1,
            command=self.send_message,
        )

        self.result = tk.Label(
            text="Click RED",
            foreground="red",
            font=("Arial", 25),  # Set the text color to white
        )

        self.frame_2 = tk.Frame(height=10)

        self.result_1 = tk.Label(
            foreground="green", font=("Arial", 25)  # Set the text color to white
        )

    def play(self):

        for children in self.window.children:
            self.window.children[children].pack()

        self.window.after(3000, self.timer_update)

        self.window.mainloop()

    def send_message(self):

        if not self.timer:
            self.false_clicks += 1
            self.result.config(text=f'Bad click count - {self.false_clicks}')
            return

        end = time()

        click_time = round(end - self.timer, 3)
        self.result_1.config(text=f'Click after - {click_time}')
        self.label.config(bg="black")
        self.timer = 0

    def timer_update(self):

        new_color = random.choice(self.colors)
        
        if new_color == "red":
            self.timer = time()

        self.label.config(bg=new_color)

        self.window.after(random.choice(range(1500, 4000)), self.timer_update)


TimerCalculator().play()


