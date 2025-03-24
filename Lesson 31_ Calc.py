from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    global expression
    total = str(eval(expression))
    equation.set(total)
    expression = ""
 

def clear():
    global expression 
    expression = "" 
    equation.set("") 
    

if __name__ == "__main__":
    
    gui = Tk()
    
    gui.configure(background="midnight blue")
    gui.title("Calc")
    gui.geometry("270x270")
    
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    
    expression_field.grid(columnspan=4,ipadx=70)
    
    button1 = Button(gui, text="1", fg="black", bg="light blue", height=1, width=7, command=lambda:press(1))
    button1.grid(row=2, column=0)
    
    button2 = Button(gui, text="2", fg="black", bg="light blue", height=1, width=7, command=lambda:press(2))
    button2.grid(row=2, column=1)
    
    button3 = Button(gui, text="3", fg="black", bg="light blue", height=1, width=7, command=lambda:press(3))
    button3.grid(row=2, column=2)
    
    button2 = Button(gui, text="4", fg="black", bg="light blue", height=1, width=7, command=lambda:press(4))
    button2.grid(row=3, column=0)
    
    button2 = Button(gui, text="5", fg="black", bg="light blue", height=1, width=7, command=lambda:press(5))
    button2.grid(row=3, column=1)
    
    button2 = Button(gui, text="6", fg="black", bg="light blue", height=1, width=7, command=lambda:press(6))
    button2.grid(row=3, column=2)
    
    button2 = Button(gui, text="7", fg="black", bg="light blue", height=1, width=7, command=lambda:press(7))
    button2.grid(row=4, column=0)
    
    button2 = Button(gui, text="8", fg="black", bg="light blue", height=1, width=7, command=lambda:press(8))
    button2.grid(row=4, column=1)
    
    button2 = Button(gui, text="9", fg="black", bg="light blue", height=1, width=7, command=lambda:press(9))
    button2.grid(row=4, column=2)
    
    button2 = Button(gui, text="0", fg="black", bg="light blue", height=1, width=7, command=lambda:press(0))
    button2.grid(row=5, column=0)
    

   
    
    plus = Button(gui, text="+", fg="black", bg='light blue', height= 1, width=7 ,command=lambda:press("+"))
    plus.grid(row=2, column=4)
    multiplication = Button(gui, text="*", fg="black", bg='light blue', height= 1, width=7 ,command=lambda:press("*"))
    multiplication.grid(row=4, column=4)
    devision = Button(gui, text="/", fg="black", bg='light blue', height= 1, width=7 ,command=lambda:press("/"))
    devision.grid(row=5, column=4)
    equal = Button(gui, text="=", fg="black", bg='light blue', height= 1, width=7 ,command=equalpress)
    equal.grid(row=5, column=2)
    minus = Button(gui, text="-", fg="black", bg='light blue', height= 1, width=7 ,command=lambda:press("-"))
    minus.grid(row=3, column=4) 
    clear = Button(gui, text="clear", fg="black", bg='light blue', height= 1, width=7 ,command=clear)
    clear.grid(row=5, column=1)
    
gui.mainloop()