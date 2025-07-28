# this was empty file, have added other tkinter quiz here to be modified later
# Importing necessary modules
import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style  

quiz_data = [
    {
        "question": "a",
        "choices": ["aa", "ab", "ac"],
        "answer": "aa"
    },
    {
        "question": "hi",
        "choices": ["ba", "bb", "cb"],
        "answer": "ba"
    },
    {
        "question": "yes",
        "choices": ["ca", "cb", "cc"],
        "answer": "ca"
    },
    {
        "question": "uh",
        "choices": ["da", "db", "dc"],
        "answer": "da"
    },
    {
        "question": "wassup'",
        "choices": ["ea", "eb", "ec"],
        "answer": "ea"
    },
    {
        "question": "how gay am i",
        "choices": ["fa", "fb", "fc"],
        "answer": "fb"
    }
]

# Displays current question and choices
def show_question():
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    choices = question["choices"]
    for i in range(len(choices)):  # Ensuring proper indexing
        choice_btns[i].config(text=choices[i], state="normal")

    feedback_label.config(text="")
    next_btn.config(state="disabled")

# Function to check answer and give feedback
def check_answer(choice):
    global score  # Declaring score as global variable

    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    if selected_choice == question["answer"]:
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct! Hellll yea:)", foreground="green")
    else:
        feedback_label.config(text="Incorrect, oopsie", foreground="red")

    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

# Move to next question
def next_question():
    global current_question  
    current_question += 1

    if current_question < len(quiz_data):
        show_question()
    else:
        messagebox.showinfo("Quiz Finished", 
                            "Quiz finished. Final score {}/{}".format(score, len(quiz_data)))
        root.destroy()

# Creating main window
root = tk.Tk()
root.title("Quizzz test:)")
root.geometry("600x500")
style = Style(theme="flatly")

# Font size adjustments
style.configure("TLabel", font=("Century", 20))
style.configure("TButton", font=("Century", 17))

# Creating question label
qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)
qs_label.pack(pady=10)

# Creating choice buttons
choice_btns = []
for i in range(3):  # Adjusted to match choices in quiz_data
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

# Feedback label
feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

# Initializing score
score = 0

# Creating score label
score_label = ttk.Label(
    root,  
    text="Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

# Creating the next question button
next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)
next_btn.pack(pady=10)

# Start current question index
current_question = 0

# Show first question
show_question()

# Start main event loop
root.mainloop()