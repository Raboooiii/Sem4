import math

def f(x):
    return x*x*x + x*x - 1

def g(x):
    return 1 / math.sqrt(1 + x)

def fixedPointIteration(equation, x0, e, N):
   
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = equation(x0)  # Evaluate the function at the current value
        print(f'Iteration-{step}, x1 = {x1:.6f} and f(x1) = {f(x1):.6f}')
        x0 = x1

        step += 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(f(x1)) > e

    if flag == 1:
        print(f'\nRequired root is: {x1:.8f}')
    else:
        print('\nNot Convergent.')

# Input Section for function, initial guess, error tolerance, and max iterations
equation_input = input('Enter the function g(x) in terms of x (e.g., (1/(1+x))**0.5): ')
x0 = float(input('Enter Initial Guess: '))
e = float(input('Tolerable Error: '))
N = int(input('Maximum Iterations: '))

# Convert the input function to a lambda function
g_expr = eval("lambda x: " + equation_input)

# Call the fixed-point iteration function
fixedPointIteration(g_expr, x0, e, N)
