import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        # Get the numbers from the entry fields
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        # Perform the chosen operation
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation")

        # Display the result
        messagebox.showinfo("Result", f"The result is: {result}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create input fields and labels
label_num1 = tk.Label(window, text="Enter first number:")
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack()

label_num2 = tk.Label(window, text="Enter second number:")
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()

# Create a variable to store the operation choice
operation_var = tk.StringVar(window)
operation_var.set("Add")  # Default value

# Create dropdown for operation choice
operation_label = tk.Label(window, text="Select operation:")
operation_label.pack()
operation_menu = tk.OptionMenu(window, operation_var, "Add", "Subtract", "Multiply", "Divide")
operation_menu.pack()

# Create the calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Run the application
window.mainloop()
