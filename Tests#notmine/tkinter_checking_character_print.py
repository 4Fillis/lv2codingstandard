import tkinter as tk

def display_char(index=0):
    if index < len(text_to_display):
        text_label.config(text=text_label.cget("text") + text_to_display[index])
        window.after(100, display_char, index + 1)

window = tk.Tk()
window.title("Character Display")

text_label = tk.Label(window, text="", font=("Helvetica", 16))
text_label.pack(padx=20, pady=20)

text_to_display = "This is a sample text."

display_char()

window.mainloop()