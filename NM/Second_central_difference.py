import math

def second_central_difference(f, x, h):
    return (f(x + h) - 2*f(x) + f(x - h))/(h**2)

function = input("Enter the function f(x) [math.sin(x) or x**2]: ")
x_input = (input("Enter the value of x: "))
h = float(input("Enter the step size h: "))

f = lambda x: eval(function)
x = eval(x_input)

derivative = second_central_difference(f, x, h)
print(f"f(x) at x = {x}: {derivative}")
