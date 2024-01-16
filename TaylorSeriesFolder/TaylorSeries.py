'''This application calculates and graphs the Taylor Series approximations of different polynomials
of the fifth degree or less. It is a very helpful tool in Calculus 1, 2 and 3 for completing questions,
visualizing solutions, and building a better understanding of mathemtical concepts. Although it is
quite a straight-forward program, there are no popular equivalents of this application available online.
Instructions: enter the coefficients of the polynomial of interest; observe the GUI for the resulting
graph and the console for the corresponding equation.'''

# Imports
import numpy as np
import time
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import decimal

# Constants
BOX_WIDTH = 3
BOX_HEIGHT = 3
CENTER_RANGE = 2
DELAY = 0.25
ROUNDING = ".001"
GRAPH_DOMAIN = 5
GRAPH_RANGE = 100
INTERVALS = 100

# Calculates the terms of the Taylor Series, given the polynomial coefficients and approximation's center
def terms_calculation(a, b, c, d, e, f, A):
        
    global Term1
    global Term2
    global Term3
    global Term4
    global Term5
    global Term6
        
    Term1 = a*A**5 + b*A**4 + c*A**3 + d*A**2 + e*A + f
        
    a = 5*a
    b = 4*b
    c = 3*c
    d = 2*d
        
    Term2 = a*A**4 + b*A**3 + c*A**2 + d*A + e
        
    a = 4*a
    b = 3*b
    c = 2*c
        
    Term3 = (a*A**3 + b*A**2 + c*A + d)/2
        
    a = 3*a
    b = 2*b
        
    Term4 = (a*A**2 + b*A + c)/(3*2)
        
    a = 2*a
        
    Term5 = (a*A + b)/(4*3*2)
    Term6 = a/(5*4*3*2)
        
# Layout of the GUI window
layout = [  [sg.Text("Input the coefficients, as decimals, for your polynomial in the spaces below, insert a zero if that term is not present. ")],
            [sg.Input(size=(BOX_WIDTH, BOX_HEIGHT)), sg.Text("x^5 + "), sg.Input(size=(BOX_WIDTH, BOX_HEIGHT)), sg.Text("x^4 + "),
             sg.Input(size=(BOX_WIDTH, BOX_HEIGHT)), sg.Text("x^3 + "), sg.Input(size=(BOX_WIDTH, BOX_HEIGHT)), sg.Text("x^2 + "),
             sg.Input(size=(BOX_WIDTH, BOX_HEIGHT)), sg.Text("x +"), sg.Input(size=(BOX_WIDTH, BOX_HEIGHT))],
            [sg.Text("")],
            [sg.Text("Please input the x coordinate (from -2 to 2) where you would like the series to be centered: ")],
            [sg.Input(size=(BOX_WIDTH + 2, BOX_HEIGHT))],
            [sg.Text("")],
            [sg.Text("Click all of the term approximations that you would like to see on the graph.")],
            [sg.Checkbox('Term 1'), sg.Checkbox('Term 2'), sg.Checkbox('Term 3')],
            [sg.Checkbox('Term 4'), sg.Checkbox('Term 5'), sg.Checkbox('Term 6')],
            [sg.Text("")],
            [sg.Button('Enter'), sg.Button('Clear'), sg.Button('Close')] ]

window = sg.Window('Inputing Values', layout)

# Draws graph on GUI prior to plotting
fig, ax = plt.subplots()
fig.show()

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Graph of Taylor Series Approximations')

ax.set_xlim(-GRAPH_DOMAIN, GRAPH_DOMAIN)
ax.set_ylim(-GRAPH_RANGE, GRAPH_RANGE)

ax.grid()

# Continuously check if the polynomial is updated until loop terminates
while True: 
    event, values = window.read()

    ax.clear() # Clears the previous graph if applicable
    print("")
    print("")
    print("")
    
    # Collects and converts the user inputs into floats
    a = float(values[0])
    b = float(values[1])
    c = float(values[2])
    d = float(values[3])
    e = float(values[4])
    f = float(values[5])
    center = float(values[6])

    if center < -CENTER_RANGE or center > CENTER_RANGE: # Handles invalid user inputs
        print("")
        print("Error, the selected coordinate is out of range")
        exit()
    else:
        A = center
        print("")
        time.sleep(DELAY)

    print("The Taylor Series of f(x), centered around point x = A, is estimated as f(x) = (f(A))/0! + (f'(A)(x-A))/1! + (f''(A)(x-A)^2)/2! ... ")
    print("")
    time.sleep(DELAY)

    print("The Taylor Series of P(x), centered around {0}, is of the form P(x) = (P({0}))/0! + (P'({0})(x-{0}))/1! + (P''({0})(x-{0})^2)/2! ..." .format(A))
    print("")
    time.sleep(DELAY)

    terms_calculation(a, b, c, d, e, f, A) # Calculates terms of the Taylor Series

    # Truncates all terms to 3 decimals
    truncate1 = decimal.Decimal(str(Term1)).quantize(decimal.Decimal(ROUNDING), rounding=decimal.ROUND_DOWN)
    Term1 = float(truncate1)
    truncate2 = decimal.Decimal(str(Term2)).quantize(decimal.Decimal(ROUNDING), rounding=decimal.ROUND_DOWN)
    Term2 = float(truncate2)
    truncate3 = decimal.Decimal(str(Term3)).quantize(decimal.Decimal(ROUNDING), rounding=decimal.ROUND_DOWN)
    Term3 = float(truncate3)
    truncate4 = decimal.Decimal(str(Term4)).quantize(decimal.Decimal(ROUNDING), rounding=decimal.ROUND_DOWN)
    Term4 = float(truncate4)
    truncate5 = decimal.Decimal(str(Term5)).quantize(decimal.Decimal(ROUNDING), rounding=decimal.ROUND_DOWN)
    Term5 = float(truncate5)
    truncate6 = decimal.Decimal(str(Term6)).quantize(decimal.Decimal(ROUNDING), rounding=decimal.ROUND_DOWN)
    Term6 = float(truncate6)

    print("The explicit Taylor Series is given by: P(x) = {0} + {1}(x-{2}) + {3}(x-{2})^2 + {4}(x-{2})^3 + {5}(x-{2})^4 + {6}(x-{2})^5 " .format(Term1, Term2, A, Term3, Term4, Term5, Term6))

    # Defines the different TS approximation equations to be graphed 
    x = np.linspace(-GRAPH_DOMAIN, GRAPH_DOMAIN, INTERVALS)
    y = a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f
    
    x1 = [-GRAPH_DOMAIN, GRAPH_DOMAIN]
    y1 = [Term1, Term1]

    x2 = [-GRAPH_DOMAIN,GRAPH_DOMAIN]
    y2 = [Term1 + Term2*(-GRAPH_DOMAIN-A), Term1 + Term2*(GRAPH_DOMAIN-A)]

    x3 = np.linspace(-GRAPH_DOMAIN, GRAPH_DOMAIN, INTERVALS)
    y3 = Term1 + Term2*(x3-A) + Term3*(x3-A)**2

    x4 = np.linspace(-GRAPH_DOMAIN, GRAPH_DOMAIN, INTERVALS)
    y4 = Term1 + Term2*(x4-A) + Term3*(x4-A)**2 + Term4*(x4-A)**3

    x5 = np.linspace(-GRAPH_DOMAIN, GRAPH_DOMAIN, INTERVALS)
    y5 = Term1 + Term2*(x5-A) + Term3*(x5-A)**2 + Term4*(x5-A)**3 + Term5*(x5-A)**4

    x6 = np.linspace(-GRAPH_DOMAIN, GRAPH_DOMAIN, INTERVALS)
    y6 = Term1 + Term2*(x6-A) + Term3*(x6-A)**2 + Term4*(x6-A)**3 + Term5*(x6-A)**4 + Term6*(x6-A)**5

    ax.plot(x, y, color = 'black', label = "Intial function")

    # Plots the TS approximations of interest if their boxes are checked
    if values[7] == True:
        ax.plot(x1, y1, color = 'red', label = "1 term approx.")
    if values[8] == True:
        ax.plot(x2, y2, color = 'lightskyblue', label = "2 term approx.")
    if values[9] == True:
        ax.plot(x3, y3, color = 'limegreen', label = "3 term approx.")
    if values[10] == True:
        ax.plot(x4, y4, color = 'yellow', label = "4 term approx.")
    if values[11] == True:
        ax.plot(x5, y5, color = 'purple', label = "5 term approx.")
    if values[12] == True:
        ax.plot(x6, y6, color = 'orange', linestyle = ":", label = "6 term approx.")
    
    # Sets the domain and range to be displayed on the graph
    ax.set_xlim(-GRAPH_DOMAIN, GRAPH_DOMAIN)
    ax.set_ylim(-GRAPH_RANGE, GRAPH_RANGE)

    plt.legend()
    ax.grid()
    
    fig.savefig("figure.pdf")
    fig.show()
    
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Equation with Taylor Series approximations')

    if event == "Clear": # Clears the equations but maintains graph structure 
        ax.clear()
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('Equation with Taylor Series approximations')
        ax.set_xlim(-GRAPH_DOMAIN, GRAPH_DOMAIN)
        ax.set_ylim(-GRAPH_RANGE, GRAPH_RANGE)
        ax.grid()
        
    if event == "Close":
        window.close()
        exit()