mport tkinter as tk
def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operation"

    result_label.config(text="Result: " + str(result))
root = tk.Tk()
root.title("Simple Calculator")
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)
operations = ["+", "-", "*", "/"]
operation_var = tk.StringVar(root)
operation_var.set("+")  # Default operation
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.pack(pady=5)
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=5)
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)
root.mainloop()