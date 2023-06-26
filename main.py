import tkinter as tk
from tkinter import DISABLED, NORMAL
from tkinter import messagebox
import json
import time

root = tk.Tk()
root.title('Typing Speed Test')
root.config(bg='#4F709C')
root.geometry('1200x900')
current_time= 60
try:
    with open('data.txt', 'r') as score_file:
        score= int(score_file.read())
except:
    score=0

def start_timer():



    global current_time

    start_btn.config(state=DISABLED)
    if current_time>0:
        if current_time>1:
            time_left_label.after(ms=1000, func=start_timer)

        time_left_label.config(text=f'Time left: {current_time-1}')
        current_time -= 1
    if current_time==0:
        calculate_speed()


def calculate_speed():
    global score
    typed_words = len(typed_data.get('1.0', tk.END).split(' '))

    typing_speed = typed_words
    if typing_speed> score:
        score= typing_speed
        with open('data.txt', 'w') as file:
            file.write(str(typing_speed))
        high_score.config(text=f'High Score: {score}')
    typed_data.config(state=NORMAL)
    start_btn.config(state=NORMAL)
    messagebox.showinfo(title='Sucess', message=f'Your speed test is successfull and your typing speed is {typing_speed}WPM')
high_score = tk.Label(text=f'High score: {score}')
high_score.pack()
name_label = tk.Label(text='Typing Speed', font=('Cursive', 40), bg='#4F709C', highlightthickness=0)
name_label.pack(pady=50)
time_left_label= tk.Label(text=f'Time Left: {current_time}', font=('Arial', 20), bg='#4F709C', highlightthickness=0)
time_left_label.pack(pady=30)
label = tk.Label(text='Type here any random words to check speed', bg='#4F709C', highlightthickness=0)
label.pack()
typed_data  = tk.Text()
typed_data.pack()

start_btn = tk.Button(text='START', bg='green', highlightthickness=0, font=('Arial', 25), command=start_timer)
start_btn.pack(pady=30)

root.mainloop()