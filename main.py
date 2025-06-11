import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Prosty Kalkulator")
        self.root.geometry("300x430")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.zrob_przyciski()

    def zrob_przyciski(self):
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        input_field = tk.Entry(
            input_frame,
            textvariable=self.input_text,
            font=('arial', 18),
            justify='right',
            bd=10,
            relief='sunken',
            state='readonly',
            readonlybackground='white'
        )
        input_field.pack(ipady=10, fill='x')

        btns_frame = tk.Frame(self.root)
        btns_frame.pack()

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]

        for row_idx, row in enumerate(buttons):
            for col_idx, char in enumerate(row):
                button = tk.Button(
                    btns_frame,
                    text=char,
                    width=5,
                    height=2,
                    font=('arial', 16),
                    command=lambda ch=char: self.klikniecie(ch)
                )
                button.grid(row=row_idx, column=col_idx, padx=5, pady=5, sticky='nsew')

        clear_btn = tk.Button(
            self.root,
            text='C',
            font=('arial', 16),
            bg='red',
            fg='white',
            height=2,
            command=self.clear_expression
        )
        clear_btn.pack(fill='x', padx=10, pady=10)

    def klikniecie(self, char):
        if char == "=":
            try:
                result = str(eval(self.expression))
                self.expression = result
            except DzieleniePrzezZero:
                messagebox.showerror("Błąd", "Nie można dzielić przez zero.")
                self.expression = ""
            except Exception:
                messagebox.showerror("Błąd", "Nieprawidłowe wyrażenie.")
                self.expression = ""
        else:
            self.expression += str(char)
        self.input_text.set(self.expression)

    def clear_expression(self):
        self.expression = ""
        self.input_text.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
