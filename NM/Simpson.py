#Approximate value of definite integral using simpson 1/3 rule
import math

def simpson( f, a, b, n):
    h = (b-a)/n
    result = f(a) + f(b)

    for i in range (1,n):
        x = a + i*h
        if i%2 == 0:
            result += 2*f(x)
        else:
            result += 4*f(x)
    
    result *= h/3

    return result

function = input("Enter the function f(x) [math.sin(x) or x**2]: ")
a = eval(input("Enter the value of Lower limit: "))
b = eval(input("Enter the value of Upper limit: "))
n = eval(input("Enter the number of subintervals [even number]: "))

f = lambda x: eval(function)

approximate = simpson(f, a, b, n)
print(f"Approximate Integral Value: {approximate}")