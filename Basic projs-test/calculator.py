
import tkinter as tk
from tkinter import *



value = ""

def press(num):
    global value
    value+=str(num)
    equation.set(value)

def equalonpress():
    try:
        global value
        answer=str(eval(value))
        equation.set(answer)
        value=""
    
    except:
        equation.set("error")
        value=""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":

    calc=Tk()
    calc.geometry("1500x1700")
    calc.title("Simple Calc")
    calc.configure(background="black")
    equation = StringVar()


    expression_field= Entry(calc, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=200)
    button1 = Button(calc, text=' 1 ', fg='white', bg='red',command=lambda: press(1), height=5, width=14)
    button1.grid(row=2, column=0)
    button2 = Button(calc, text=' 2 ', fg='black', bg='pink',command=lambda: press(2), height=5, width=14)
    button2.grid(row=2, column=1)
    button3 = Button(calc, text=' 3 ', fg='white', bg='red',command=lambda: press(3), height=5, width=14)
    button3.grid(row=2, column=2)
    button4 = Button(calc, text=' 4 ', fg='black', bg='pink',command=lambda: press(4), height=5, width=14)
    button4.grid(row=3, column=0)
    button5 = Button(calc, text=' 5 ', fg='white', bg='red',command=lambda: press(5), height=5, width=14)
    button5.grid(row=3, column=1)
    button6 = Button(calc, text=' 6 ', fg='black', bg='pink',command=lambda: press(6), height=5, width=14)
    button6.grid(row=3, column=2)
    button7 = Button(calc, text=' 7 ', fg='white', bg='red',command=lambda: press(7), height=5, width=14)
    button7.grid(row=4, column=0)
    button8 = Button(calc, text=' 8 ', fg='black', bg='pink',command=lambda: press(8), height=5, width=14)
    button8.grid(row=4, column=1)
    button9 = Button(calc, text=' 9 ', fg='white', bg='red',command=lambda: press(9), height=5, width=14)
    button9.grid(row=4, column=2)
    button0 = Button(calc, text=' 0 ', fg='black', bg='pink',command=lambda: press(0), height=5, width=14)
    button0.grid(row=5, column=0)
    plus = Button(calc, text=' + ', fg='black', bg='pink',command=lambda: press("+"), height=5, width=14)
    plus.grid(row=2, column=3)
    minus = Button(calc, text=' - ', fg='white', bg='red',command=lambda: press("-"), height=5, width=14)
    minus.grid(row=3, column=3)
    multiply = Button(calc, text=' * ', fg='black', bg='pink',command=lambda: press("*"), height=5, width=14)
    multiply.grid(row=4, column=3)
    divide = Button(calc, text=' / ', fg='white', bg='red',command=lambda: press("/"), height=5, width=14)
    divide.grid(row=5, column=3)
    equalonpress = Button(calc, text=' = ', fg='black', bg='pink',
    command=equalonpress, height=5, width=14)
    equalonpress.grid(row=5, column=2)
    clear = Button(calc, text='Clear', fg='white', bg='red',
    command=clear, height=5, width=14)
    clear.grid(row=5, column='1')
    Decimal= Button(calc, text='.', fg='white', bg='red',
    command=lambda: press('.'), height=5, width=14)
    Decimal.grid(row=6, column=0)


    calc.mainloop()      



