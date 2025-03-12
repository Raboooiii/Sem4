#Approximate value of definite integral using boole's rule
import math

def Boole( f, a, b):
    h = (b-a)/4
    x = [a + i*h for i in range (5)]
    result = 7*f(x[0]) + 32*f(x[1]) + 12*f(x[2]) + 32*f(x[3]) + 7*f(x[4])

    result *= 2*h/45

    return result

function = input("Enter the function f(x) [math.sin(x) or x**2]: ")
a = eval(input("Enter the value of Lower limit: "))
b = eval(input("Enter the value of Upper limit: "))

f = lambda x: eval(function)

approximate = Boole(f, a, b)
print(f"Approximate Integral Value: {approximate}")