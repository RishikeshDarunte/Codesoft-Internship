import tkinter as tk
from tkinter import messagebox, font

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x500")
        self.root.configure(bg="#f2f2f2")

        # Create a custom font
        self.custom_font = font.Font(family="Helvetica", size=12)

        self.tasks = []
        self.task_var = tk.StringVar()

        # Entry Box
        self.task_entry = tk.Entry(root, textvariable=self.task_var, width=30, font=self.custom_font, 
                                    bg="#ffffff", fg="#333333", insertbackground='black')
        self.task_entry.pack(pady=20)
        self.task_entry.insert(0, "Enter the task")
        self.task_entry.bind("<FocusIn>", self.on_entry_click)
        self.task_entry.bind("<FocusOut>", self.on_focus_out)

        # Listbox
        self.task_listbox = tk.Listbox(root, height=15, width=45, font=self.custom_font, 
                                        bg="#ffffff", fg="#333333", selectbackground="#cce7ff")
        self.task_listbox.pack(pady=10)

        # Buttons with improved styling
        self.add_task_button = tk.Button(root, text="Add Task", width=15, command=self.add_task, 
                                          bg="#4CAF50", fg="white", font=self.custom_font)
        self.add_task_button.pack(pady=5)

        self.update_task_button = tk.Button(root, text="Update Task", width=15, command=self.update_task, 
                                             bg="#2196F3", fg="white", font=self.custom_font)
        self.update_task_button.pack(pady=5)

        self.delete_task_button = tk.Button(root, text="Delete Task", width=15, command=self.delete_task, 
                                             bg="#f44336", fg="white", font=self.custom_font)
        self.delete_task_button.pack(pady=5)

        self.complete_task_button = tk.Button(root, text="Mark as Complete", width=15, command=self.complete_task, 
                                               bg="#FF9800", fg="white", font=self.custom_font)
        self.complete_task_button.pack(pady=5)

    def on_entry_click(self, event):
        """Function to handle entry click."""
        if self.task_entry.get() == "Enter the task":
            self.task_entry.delete(0, tk.END)  # Delete all the text in the entry
            self.task_entry.config(fg="#333333")  # Change text color

    def on_focus_out(self, event):
        """Function to handle focus out."""
        if self.task_entry.get() == "":
            self.task_entry.insert(0, "Enter the task")
            self.task_entry.config(fg="#999999")  # Change text color to indicate placeholder

    def add_task(self):
        task = self.task_var.get()
        if task and task != "Enter the task":
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = self.task_var.get()
            if new_task and new_task != "Enter the task":
                self.tasks[selected_task_index[0]] = new_task
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, new_task)
                self.task_var.set("")
            else:
                messagebox.showwarning("Warning", "You must enter a new task.")
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            self.tasks[selected_task_index[0]] = f"{task} (Completed)"
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(selected_task_index, f"{task} (Completed)")
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as complete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
