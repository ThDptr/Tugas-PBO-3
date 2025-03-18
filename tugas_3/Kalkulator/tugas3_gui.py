import tkinter as tk
from tkinter import messagebox
import math

class Number:
    """Kelas untuk menyimpan nilai dan menggunakan Dunder Methods"""
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __truediv__(self, other):
        return Number(self.value / other.value)

    def __pow__(self, other):
        return Number(self.value ** other.value)

    @staticmethod
    def log(number, base):
        return Number(math.log(number.value, base.value))

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator with Dunder Methods")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.current_input = ""
        self.result_var = tk.StringVar()

        self.create_display()
        self.create_buttons()

    def create_display(self):
        display_frame = tk.Frame(self.root, height=50)
        display_frame.pack(fill=tk.X, padx=10, pady=10)

        display = tk.Entry(display_frame, textvariable=self.result_var, 
                          font=("Arial", 18), bd=10, relief=tk.RIDGE, justify=tk.RIGHT)
        display.pack(fill=tk.BOTH, expand=True)

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/', '(',
            '4', '5', '6', '*', ')',
            '1', '2', '3', '-', ',',
            '0', '.', 'C', '+', '^',
            'log', '='
        ]

        row, col = 0, 0
        for button_text in buttons:
            if button_text == '=':
                btn = tk.Button(button_frame, text=button_text, font=("Arial", 14), 
                               bg="lightblue", command=self.calculate_result)
                btn.grid(row=row, column=col, columnspan=2, sticky="nsew")
                col += 1
            else:
                btn = tk.Button(button_frame, text=button_text, font=("Arial", 14),
                               command=lambda t=button_text: self.on_button_click(t))
                btn.grid(row=row, column=col, sticky="nsew")
            
            col += 1
            if col > 4:
                col = 0
                row += 1

        for i in range(5):
            button_frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)

    def on_button_click(self, text):
        if text == 'C':
            self.current_input = ""
            self.result_var.set("")
        else:
            self.current_input += str(text)
            self.result_var.set(self.current_input)

    def parse_expression(self, expr):
        """Mengurai ekspresi dan mengembalikan stack untuk evaluasi"""
        # Implementasi parser yang lebih kompleks diperlukan untuk skala penuh
        try:
            if 'log' in expr:
                base, num = expr.split(',')
                base = base.replace('log(', '')
                num = num.replace(')', '')
                return Number.log(Number(float(num)), Number(float(base)))
            else:
                parts = expr.split('^')
                if len(parts) == 2:
                    return Number(float(parts[0])) ** Number(float(parts[1]))
        except:
            raise ValueError("Invalid expression")
        
        ops = {'+': Number.__add__, '-': Number.__sub__,
               '*': Number.__mul__, '/': Number.__truediv__}
        for op in ops:
            if op in expr:
                a, b = expr.split(op)
                return ops[op](Number(float(a)), Number(float(b)))
        
        return Number(float(expr))

    def calculate_result(self):
        try:
            # Parsing manual untuk demonstrasi Dunder Methods
            result = self.parse_expression(self.current_input)
            self.result_var.set(str(result.value))
            self.current_input = str(result.value)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Input: {str(e)}")
            self.current_input = ""
            self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()