import tkinter as tk
from tkinter import messagebox
import sqlite3

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List with Database")
        self.root.geometry("500x400")

        # Database setup
        self.db_connection = sqlite3.connect("todo_list.db")
        self.db_cursor = self.db_connection.cursor()
        self.create_table()

        # Task Input
        self.entry_label = tk.Label(root, text="Enter a new task:")
        self.entry_label.pack(pady=5)
        
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=5)

        # Buttons
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="green", fg="white")
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Selected Task", command=self.delete_task, bg="red", fg="white")
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Mark as Complete", command=self.mark_complete, bg="blue", fg="white")
        self.complete_button.pack(pady=5)

        # Task List
        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        # Load tasks from database
        self.load_tasks()

    def create_table(self):
        """Create the tasks table if it doesn't already exist."""
        self.db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'Pending'
            )
        """)
        self.db_connection.commit()

    def add_task(self):
        """Add a new task to the database and listbox."""
        task = self.entry.get()
        if task.strip():
            self.db_cursor.execute("INSERT INTO tasks (task, status) VALUES (?, ?)", (task, 'Pending'))
            self.db_connection.commit()
            self.task_listbox.insert(tk.END, f"{task} (Pending)")
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        """Delete the selected task from the database and listbox."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            selected_task = self.task_listbox.get(selected_index)
            task_name = selected_task.split(" (")[0]

            # Delete from database
            self.db_cursor.execute("DELETE FROM tasks WHERE task = ?", (task_name,))
            self.db_connection.commit()

            # Remove from listbox
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete!")

    def mark_complete(self):
        """Mark the selected task as complete in the database and update the listbox."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            selected_task = self.task_listbox.get(selected_index)
            task_name = selected_task.split(" (")[0]

            # Update status in database
            self.db_cursor.execute("UPDATE tasks SET status = 'Completed' WHERE task = ?", (task_name,))
            self.db_connection.commit()

            # Update listbox
            self.task_listbox.delete(selected_index)
            self.task_listbox.insert(tk.END, f"{task_name} (Completed)")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as complete!")

    def load_tasks(self):
        """Load all tasks from the database into the listbox."""
        self.db_cursor.execute("SELECT task, status FROM tasks")
        tasks = self.db_cursor.fetchall()
        for task, status in tasks:
            self.task_listbox.insert(tk.END, f"{task} ({status})")

    def close_app(self):
        """Close the database connection when the app is closed."""
        self.db_connection.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.protocol("WM_DELETE_WINDOW", app.close_app)
    root.mainloop()
