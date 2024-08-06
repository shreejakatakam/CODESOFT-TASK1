import tkinter as tk
tasks = []
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def complete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        listbox.delete(index)
    except IndexError:
        pass

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        pass
root = tk.Tk()
root.title("To-Do List App")


entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

complete_button = tk.Button(root, text="Mark as Completed", command=complete_task)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

root.mainloop()

