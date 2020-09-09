#!/usr/bin/env python3

from tkinter import *
from tkinter import font

root = Tk()
root.title("Calculator")
root.configure(background="grey")
myFont = font.Font(size=20)
myFont2 = font.Font(size=25, family="Uroob")
scoreFont = font.Font(size=30, family="Uroob")
clearFont = font.Font(size=10)
sumNumber = 0
operationMark = "+"

def button_click(number):
    if number == ".":
        float(calculation.get())
    try:
        float(calculation.get())
    except ValueError:
        calculation.delete(0, END)
    calculation.insert(END, number)
    return

def sumUp():
    global sumNumber
    global operationMark
    if operationMark == "+":
        try:
            sumNumber += float(calculation.get())
            if sumNumber.is_integer():
                sumNumber = int(sumNumber)
        except ValueError:
            pass
    elif operationMark == "-":
        try:
            sumNumber -= float(calculation.get())
            if sumNumber.is_integer():
                sumNumber = int(sumNumber)
        except ValueError:
            pass
    elif operationMark == "*":
        try:
            sumNumber *= float(calculation.get())
            if sumNumber.is_integer():
                sumNumber = int(sumNumber)
        except ValueError:
            pass
    elif operationMark == "/":
        try:
            sumNumber /= float(calculation.get())
            if sumNumber.is_integer():
                sumNumber = int(sumNumber)
        except ValueError:
            pass


def changeOperationMark(operator):
    global operationMark
    calculation.delete(0, END)
    
    if operator == "+":
        operationMark = "+"
        calculation.insert(0, "+")
    elif operator == "-":
        operationMark = "-"
        calculation.insert(0, "-")
    elif operator == "*":
        operationMark = "*"
        calculation.insert(0, "*")
    elif operator == "/":
        operationMark = "/"
        calculation.insert(0, "/")

    score.delete(0, END)
    score.insert(0, sumNumber)

def operations(operator):
    sumUp()
    changeOperationMark(operator)

def equalFunc():
    global sumNumber
    sumUp()
    calculation.delete(0, END)
    score.delete(0, END)
    score.insert(0, sumNumber)

def clearFunc():
    global sumNumber
    global operationMark
    sumNumber = 0
    operationMark = "+"
    score.delete(0, END)
    calculation.delete(0, END)

#frame fro input and score

frameScore = LabelFrame(root, text='Your score', background="grey", foreground="blue", padx=10, pady=10)
frameScore.grid(padx=10, row=0, columnspan=3)
frame = LabelFrame(root, text='Calculation...', background="grey", foreground="#21bd13", padx=10, pady=10)
frame.grid(padx=10, pady=(0, 20), row=1, columnspan=3)

#creating input
calculation = Entry(frame, font=myFont2, width=30, borderwidth=3, background="black", foreground="green", highlightbackground="#21bd13")
score = Entry(frameScore, font=myFont2, width=30, borderwidth=3, background="white", foreground="blue", highlightbackground="blue")
#creating buttons
zero = Button(root, text='0', font=myFont, background="grey", highlightbackground="#bfbfbf", padx=40, pady=20, command=lambda: button_click(0))
one = Button(root, text='1', font=myFont, background="grey", highlightbackground="#bfbfbf", padx=40, pady=20, command=lambda: button_click(1))
two = Button(root, text='2', font=myFont, background="grey", highlightbackground="#bfbfbf", padx=40, pady=20, command=lambda: button_click(2))
three = Button(root, text='3', font=myFont, background="grey", highlightbackground="#bfbfbf", padx=40, pady=20, command=lambda: button_click(3))
four = Button(root, text='4', font=myFont, background="grey", highlightbackground="#bfbfbf", padx=40, pady=20, command=lambda: button_click(4))
five = Button(root, text='5', font=myFont, background="grey", highlightbackground="#bfbfbf", padx=40, pady=20, command=lambda: button_click(5))
six = Button(root, text='6', font=myFont, background="grey", highlightbackground="#bfbfbf", padx=40, pady=20, command=lambda: button_click(6))
seven = Button(root, text='7', font=myFont, background="grey", highlightbackground="#bfbfbf", padx=40, pady=20, command=lambda: button_click(7))
eight = Button(root, text='8', font=myFont, background="grey", highlightbackground="#bfbfbf", padx=40, pady=20, command=lambda: button_click(8))
nine = Button(root, text='9', font=myFont, background="grey", highlightbackground="#bfbfbf", padx=40, pady=20, command=lambda: button_click(9))
dot = Button(root, text='.', font=myFont, background="grey", highlightbackground="#bfbfbf", padx=40, pady=20, command=lambda: button_click("."))

add = Button(root, text="+", font=myFont, background="grey", highlightbackground="#bfbfbf", padx=39, pady=20, command = lambda: operations("+"))
minus = Button(root, text="-", font=myFont, background="grey", highlightbackground="#bfbfbf", padx=39, pady=20, command = lambda: operations("-"))
multiply = Button(root, text="*", font=myFont, background="grey", highlightbackground="#bfbfbf", padx=39, pady=20, command = lambda: operations("*"))
divide = Button(root, text="/", font=myFont, background="grey", highlightbackground="#bfbfbf", padx=39, pady=20, command = lambda: operations("/"))
equal = Button(root, text="=", font=myFont, background="grey", highlightbackground="#bfbfbf", padx=91, pady=20, command = equalFunc)
clear = Button(root, font=clearFont, text="AC", background="grey", highlightbackground="#bfbfbf", padx=39, pady=20, command = clearFunc)
quitButton = Button(root, text="Quit", background="grey", highlightbackground="#bfbfbf", command=root.quit)

#showing buttons using grid
calculation.grid(row=0, column=0, columnspan=3, padx=5, sticky="nsew")
score.grid(row=0, column=0, columnspan=3, padx=5, sticky="nsew")

one.grid(row=2, column=0, sticky="nsew")
two.grid(row=2, column=1, sticky="nsew")
three.grid(row=2, column=2, sticky="nsew")

four.grid(row=3, column=0, sticky="nsew")
five.grid(row=3, column=1, sticky="nsew")
six.grid(row=3, column=2, sticky="nsew")

seven.grid(row=4, column=0, sticky="nsew")
eight.grid(row=4, column=1, sticky="nsew")
nine.grid(row=4, column=2, sticky="nsew")

zero.grid(row=5, column=0, sticky="nsew")
dot.grid(row=5, column=1, sticky="nsew")

add.grid(row=6, column=0, sticky="nsew")
minus.grid(row=7, column=0, sticky="nsew")
multiply.grid(row=7, column=1, sticky="nsew")
divide.grid(row=7, column=2, sticky="nsew")
equal.grid(row=6, column=1, sticky="nsew", columnspan=2)
clear.grid(row=5, column=2, sticky="nsew")
quitButton.grid(row=8, column=0, sticky="nsew", columnspan=3)

root.mainloop()