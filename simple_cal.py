import tkinter as tk

# Window create karo
root = tk.Tk()
root.title("Simple Calculator")

# Entry box
entry = tk.Entry(root, width=25, borderwidth=5, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4)

# Button click function
def click_button(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear_button():
    entry.delete(0, tk.END)

def equal_button():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Buttons layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3)
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=5, height=2, command=equal_button).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=5, height=2, command=lambda t=text: click_button(t)).grid(row=row, column=col)

# Clear button
tk.Button(root, text="C", width=5, height=2, command=clear_button).grid(row=4, column=2)

root.mainloop()
