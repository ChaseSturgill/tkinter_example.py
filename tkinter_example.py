from tkinter import *

#Creating a basic window
window = Tk()
window.geometry("312x324") #The size of the windows: Width = 500, Height = 375
window.resizable(0, 0) #Prevents user from resizing the window
window.title("Calculator")

##################### Functions #####################

#'btn_click' function continuously updates the input field whenver you enter a number
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

#'btn_clear' function clears the input field 
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

#'btn_equal' calculates the expression present in input field
def btn_equal():
    global expression
    result = str(eval(expression)) # 'eval' function evaluates the string expression directly
    input_text.set(result)
    expression = ""

expression = ""
input_text = StringVar() #'StringVar()' is used to get the instance of the input field



window.mainloop()