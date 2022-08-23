from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("Re-Formatter")

my_list = []

def clear():
    global my_list
    my_text.delete(1.0, END)
    out_text.delete(1.0, END)
    my_list = []

def get_text():
    splitstring = my_text.get(1.0, END).split("\n")
    for x in splitstring:
        my_list.append(x)
    out_text.insert(1.0, ", ".join(my_list)[:-2])

def quit():
    root.destroy()

my_text = Text(root, width=60, height=10, font=("Helvetica", 12))
my_text.pack(pady=20)

out_text = Text(root, width=60, height=16, font=("Helvetica", 12))
out_text.pack(pady=20)

button_frame = Frame(root)
button_frame.pack()

clear_button = Button(button_frame, text="Clear", command=clear)
clear_button.grid(row=0, column=0, padx=20)

get_text_button = Button(button_frame, text="  Go  ", command=get_text)
get_text_button.grid(row=0, column=1, padx=20)

quit_button = Button(button_frame, text="Quit", command=quit)
quit_button.grid(row=0, column=2, padx=20)

root.mainloop()
