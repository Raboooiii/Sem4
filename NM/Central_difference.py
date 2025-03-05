import math

def central_difference(f, x, h):
    return (f(x + h) - f(x - h))/(2*h)

function = input("Enter the function f(x) [math.sin(x) or x**2]: ")
x_input = (input("Enter the value of x: "))
h = float(input("Enter the step size h: "))

f = lambda x: eval(function)
x = eval(x_input)

print(f"f(x) at x = {x}: {central_difference(f, x, h)}")
