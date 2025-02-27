# Program to print table of any number with GUI
import tkinter as tk

def generate_table():
    try:
        num = int(entry_var.get())
        table_text.set("\n".join([f'{num} x {i} = {num * i}' for i in range(1,11)]))
    except ValueError:
        table_text.set("Please Enter a valid number")
    



#Create main window
root = tk.Tk()
root.title('Multiplication Table Generator ~ Pranjal Tech')
root.geometry("300x400")
entry_var = tk.StringVar()
table_text= tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 18), justify="center")
entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate Table", font=("Arial", 16), command=generate_table)
generate_button.pack(pady=10)

result_label = tk.Button(root, textvariable=table_text, font=('Arial', 14),justify='left')
result_label.pack(pady=10)

root.mainloop()