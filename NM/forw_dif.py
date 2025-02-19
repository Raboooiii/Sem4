import numpy as np
import sympy as sp

def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

func_str = input("Enter the function in terms of x (e.g., x**2, np.sin(x)): ")
x = float(input("Enter the value of x: "))
h = float(input("Enter the step size h: "))

def f(x):
    return eval(func_str, {"x": x, "np": np})

approx_derivative = forward_difference(f, x, h)

x_sym = sp.Symbol('x')
f_sym = eval(func_str, {"x": x_sym, "np": sp})  
actual_derivative_expr = sp.diff(f_sym, x_sym)  
actual_derivative = actual_derivative_expr.subs(x_sym, x) 

print(f"Approximate derivative at x={x}: {approx_derivative}")
print(f"Actual derivative at x={x}: {actual_derivative}")
