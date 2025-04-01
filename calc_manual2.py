import tkinter as tk
import math

class CalculatorSelector:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Выбор калькулятора")
        self.root.geometry("300x200")
        self.root.configure(bg='#f0f0f0')
        
        label = tk.Label(self.root, 
                        text="Выберите калькулятор:", 
                        font=('Arial', 16),
                        bg='#f0f0f0')
        label.pack(pady=20)
        
        btn_standard = tk.Button(self.root, 
                               text="Стандартный", 
                               font=('Arial', 14),
                               command=self.open_standard,
                               bg='#4ECDC4',
                               width=15)
        btn_standard.pack(pady=10)
        
        btn_scientific = tk.Button(self.root, 
                                 text="Научный", 
                                 font=('Arial', 14),
                                 command=self.open_scientific,
                                 bg='#45B7D1',
                                 width=15)
        btn_scientific.pack(pady=10)
        
        self.root.mainloop()
    
    def open_standard(self):
        self.root.destroy()
        StandardCalculator()
    
    def open_scientific(self):
        self.root.destroy()
        ScientificCalculator()

class BaseCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.expression = ""
        self.equation = tk.StringVar()
        self.create_widgets()
        self.create_base_buttons()

    def create_widgets(self):
        entry = tk.Entry(self,
                        textvariable=self.equation,
                        font=('Arial', 20),
                        bg='white',
                        fg='black',
                        borderwidth=2,
                        relief='sunken',
                        justify='right')
        entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky='nsew')

    def on_button_click(self, char):
        if char == '=':
            self.calculate()
        elif char == 'Clear':
            self.clear()
        elif char == '⇄':  # Кнопка переключения
            self.switch_calculator()
        elif char == 'discr':  # Кнопка для вычисления дискриминанта
            self.calculate_discriminant()
        else:
            self.expression += str(char)
            self.equation.set(self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.equation.set(result)
            self.expression = ""
        except:
            self.equation.set(" error ")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.equation.set("")
    
    def switch_calculator(self):
        self.destroy()
        if isinstance(self, StandardCalculator):
            ScientificCalculator()
        else:
            StandardCalculator()

    def create_base_buttons(self):
        base_buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('Clear', 5, 3),
            ('discr', 6, 0)  # Кнопка для вычисления дискриминанта
        ]

        for (text, row, col) in base_buttons:
            bg_color = '#FF6B6B' if text in '+-*/=.' else '#4ECDC4'
            fg_color = 'white' if text in '+-*/=.' else 'black'

            action = lambda x=text: self.on_button_click(x)
            button = tk.Button(self,
                              text=text,
                              font=('Arial', 14),
                              fg=fg_color,
                              bg=bg_color,
                              command=action,
                              borderwidth=1,
                              relief='raised')
            button.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')

        # Добавляем кнопку переключения
        switch_btn = tk.Button(self,
                              text="⇄",
                              font=('Arial', 14),
                              command=self.switch_calculator,
                              bg='#FFA500',
                              fg='white')
        switch_btn.grid(row=7, column=4, padx=2, pady=2, sticky='nsew')

        for i in range(5):
            self.grid_columnconfigure(i, weight=1)
        for i in range(8):  # Увеличили на 1 для кнопки переключения
            self.grid_rowconfigure(i, weight=1)

    def calculate_discriminant(self):
        # Создаем новое окно для ввода коэффициентов a, b и c
        def calculate():
            try:
                a = float(entry_a.get())
                b = float(entry_b.get())
                c = float(entry_c.get())
                discriminant = b**2 - 4*a*c
                result_label.config(text=f"Дискриминант: {discriminant}")
            except ValueError:
                result_label.config(text="Некорректный ввод!")

        # Создаем новое окно для ввода коэффициентов
        discriminant_window = tk.Toplevel(self)
        discriminant_window.title("Ввод коэффициентов")
        discriminant_window.geometry("300x200")

        # Ввод коэффициентов a, b и c
        label_a = tk.Label(discriminant_window, text="Коэффициент a:")
        label_a.pack()
        entry_a = tk.Entry(discriminant_window)
        entry_a.pack()

        label_b = tk.Label(discriminant_window, text="Коэффициент b:")
        label_b.pack()
        entry_b = tk.Entry(discriminant_window)
        entry_b.pack()

        label_c = tk.Label(discriminant_window, text="Коэффициент c:")
        label_c.pack()
        entry_c = tk.Entry(discriminant_window)
        entry_c.pack()

        # Кнопка для расчета дискриминанта
        calculate_button = tk.Button(discriminant_window, text="Вычислить", command=calculate)
        calculate_button.pack(pady=10)

        # Место для отображения результата
        result_label = tk.Label(discriminant_window, text="Результат")
        result_label.pack()

class StandardCalculator(BaseCalculator):
    def __init__(self):
        super().__init__()
        self.title("Standard Calculator")
        self.geometry("300x450")  # Увеличили высоту для кнопки переключения
        self.configure(bg='#2D2D2D')
        self.minsize(250, 400)

class ScientificCalculator(BaseCalculator):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("450x550")  # Увеличили размер
        self.configure(bg='#34495E')
        self.create_scientific_buttons()
        self.minsize(400, 500)

    def calculate(self):
        try:
            self.expression = self.expression.replace('^', '**')
            result = str(self.evaluate_expression(self.expression))
            self.equation.set(result)
            self.expression = result
        except:
            self.equation.set(" error ")
            self.expression = ""

    def evaluate_expression(self, expr):
        expr = expr.replace("sin", "math.sin")
        expr = expr.replace("cos", "math.cos")
        expr = expr.replace("tan", "math.tan")
        expr = expr.replace("sqrt", "math.sqrt")
        return eval(expr)

    def create_scientific_buttons(self):
        scientific_buttons = [
            ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('log', 1, 3), ('ln', 1, 4),
            ('sqrt', 4, 4), ('^', 5, 4), ('(', 2, 4), (')', 3, 4)
        ]

        for (text, row, col) in scientific_buttons:
            action = lambda x=text: self.on_button_click(x)
            button = tk.Button(self,
                              text=text,
                              font=('Arial', 14),
                              fg='white',
                              bg='#45B7D1',
                              command=action,
                              borderwidth=1,
                              relief='raised')
            button.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')

if __name__ == "__main__":
    CalculatorSelector()
