import tkinter as tk

def get_text_content():
    content = text_area.get("1.0", "end-1c") # "end-1c" to exclude the trailing newline
    print(f"Text area content:\n{content}")

root = tk.Tk()
root.title("Multi-line Text Input Example")

label = tk.Label(root, text="Enter your message:")
label.pack()

text_area = tk.Text(root, height=5, width=30)
text_area.pack()

get_button = tk.Button(root, text="Get Text", command=get_text_content)
get_button.pack()

root.mainloop()