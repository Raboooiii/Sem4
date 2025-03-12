#Approximate value of definite integral using Weddle's rule
import math

def Weddle( f, a, b):
    h = (b-a)/6
    x = [a + i*h for i in range (7)]
    result = f(x[0]) + 5*f(x[1]) + f(x[2]) + 6*f(x[3]) + f(x[4]) + 5*f(x[5]) + f(x[6])
    
    result *= 3*h/10

    return result

function = input("Enter the function f(x) [math.sin(x) or x**2]: ")
a = eval(input("Enter the value of Lower limit: "))
b = eval(input("Enter the value of Upper limit: "))

f = lambda x: eval(function)

approximate = Weddle(f, a, b)
print(f"Approximate Integral Value: {approximate}")