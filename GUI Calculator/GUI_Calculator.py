from tkinter import *

# Root initialization
root = Tk()

# Changes title name
root.title("Calculator")

# Changes background color of Entry and other widgets
root.tk_setPalette(background="#ffb700")

# Sets icon of the calculator app, at the top left hand corner
root.iconbitmap("./calculator.ico")

# Sets the body color of the calculator
root.configure(bg="#474747")

# Sets the size of the calculator window
root.geometry("410x300")

# Initializes the input field of the calculator
e = Entry(root, width=32, borderwidth=5, font=("Arial",16), justify="right")
e.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

# Global Variables
holding_val = 0
bool_add = False
bool_subt = False
bool_mult = False
bool_div = False


def button_click(number):
    """
    Input: Number
    Takes the number, and updates the display in the calculator.
    """
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    """
    Clears the numbers on the calculator display.
    """
    e.delete(0, END)


def func_button_add():
    """
    Updates the holding value, and changes bool_add status for addition.
    """
    global holding_val, bool_add
    holding_val = e.get()
    e.delete(0, END)
    bool_add = True


def func_button_subt():
    """
    Updates the holding value, and changes bool_subt status for subtraction.
    """
    global holding_val, bool_subt 
    holding_val = e.get()
    e.delete(0, END)
    bool_subt = True


def func_button_mult():
    """
    Updates the holding value, and changes bool_mult status for multiplication.
    """
    global holding_val, bool_mult
    holding_val = e.get()
    e.delete(0, END)
    bool_mult = True


def func_button_div():
    """
    Updates the holding value, and changes bool_div status for division.
    """
    global holding_val, bool_div
    holding_val = e.get()
    e.delete(0, END)
    bool_div = True


def func_button_1byX():
    """
    Divides 1 by the number, and displays on the screen.
    """
    current = e.get()
    e.delete(0, END)
    calc_1byx = 1 / float(current)
    e.insert(0, str(calc_1byx))


def func_button_Xsquare():
    """
    Squares the number, and displays on the screen.
    """  
    current = e.get()
    e.delete(0, END)
    calc_Xsquare = float(current) ** 2
    e.insert(0, str(calc_Xsquare))


def func_button_sqrootX():
    """
    Creates the square root of the number, and displays on the screen.
    """
    current = e.get()
    e.delete(0, END)
    calc_sqrootX = float(current) ** (1/2)
    e.insert(0, str(calc_sqrootX))


def func_equalto():
    """
    Calculates the given input.
    """
    global holding_val, bool_add, bool_subt, bool_mult, bool_div
    
    # For Addition
    if bool_add == True:
        total = float(e.get()) + float(holding_val)
        e.delete(0, END)
        e.insert(0, str(total))
        holding_val = 0
        bool_add = False

    # For Subtraction
    elif bool_subt == True:
        total = float(holding_val) - float(e.get()) 
        e.delete(0, END)
        e.insert(0, str(total))
        holding_val = 0
        bool_subt = False

    # For Multiplication
    elif bool_mult == True:
        total = float(holding_val) * float(e.get()) 
        e.delete(0, END)
        e.insert(0, str(total))
        holding_val = 0
        bool_mult = False

    # For Division
    elif bool_div == True:
        total = float(holding_val) / float(e.get()) 
        e.delete(0, END)
        e.insert(0, str(total))
        holding_val = 0
        bool_div = False


# Creates the button
button_1byX = Button(root, font=("Arial",11), text="1/x", width=9, height= 2, command=func_button_1byX)
button_Xsquare = Button(root, font=("Arial",11), text="x²", width=9, height= 2, command=func_button_Xsquare)
button_sqrootX = Button(root, font=("Arial",11), text="√x", width=9, height= 2, command=func_button_sqrootX)
button_div = Button(root, font=("Arial",11), text="÷", width=9, height= 2, command=func_button_div)

button7 = Button(root, font=("Arial",11), text="7", width=9, height= 2, command=lambda: button_click(7))
button8 = Button(root, font=("Arial",11), text="8", width=9, height= 2, command=lambda: button_click(8))
button9 = Button(root, font=("Arial",11), text="9", width=9, height= 2, command=lambda: button_click(9))
button_mult = Button(root, font=("Arial",11), text="×", width=9, height= 2, command=func_button_mult)

button4 = Button(root, font=("Arial",11), text="4", width=9, height= 2, command=lambda: button_click(4))
button5 = Button(root, font=("Arial",11), text="5", width=9, height= 2, command=lambda: button_click(5))
button6 = Button(root, font=("Arial",11), text="6", width=9, height= 2, command=lambda: button_click(6))
button_subt = Button(root, font=("Arial",11), text="-", width=9, height= 2, command=func_button_subt)

button1 = Button(root, font=("Arial",11), text="1", width=9, height= 2, command=lambda: button_click(1))
button2 = Button(root, font=("Arial",11), text="2", width=9, height= 2, command=lambda: button_click(2))
button3 = Button(root, font=("Arial",11), text="3", width=9, height= 2, command=lambda: button_click(3))
button_add = Button(root, font=("Arial",11), text="+", width=9, height= 2, command=func_button_add)

button_clear = Button(root, font=("Arial",11), text="CLR", width=9, height= 2, command=button_clear)
button0 = Button(root, font=("Arial",11), text="0", width=9, height= 2, command=lambda: button_click(0))
button_dot = Button(root, font=("Arial",11), text=".", width=9, height= 2, command=lambda: button_click("."))
button_equalto = Button(root, font=("Arial",11), text="=", width=9, height= 2, command=func_equalto, bg="#d00000")

# Sets the position of the buttons
button_1byX.grid(row=1, column=1)
button_Xsquare.grid(row=1, column=2)
button_sqrootX.grid(row=1, column=3)
button_div.grid(row=1, column=4)

button7.grid(row=2, column=1)
button8.grid(row=2, column=2)
button9.grid(row=2, column=3)
button_mult.grid(row=2, column=4)

button4.grid(row=3, column=1)
button5.grid(row=3, column=2)
button6.grid(row=3, column=3)
button_subt.grid(row=3, column=4)

button1.grid(row=4, column=1)
button2.grid(row=4, column=2)
button3.grid(row=4, column=3)
button_add.grid(row=4, column=4)

button_clear.grid(row=5, column=1)
button0.grid(row=5, column=2)
button_dot.grid(row=5, column=3)
button_equalto.grid(row=5, column=4)

# Runs the main loop of the program
root.mainloop()
