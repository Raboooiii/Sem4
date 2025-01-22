def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            print("Derivative is zero. No solution found.")
        
        x_new = x - fx / dfx
        
        if abs(x_new - x) < tol:
            return x_new
        
        x = x_new
    
    raise ValueError("Maximum iterations reached. No solution found.")

if __name__ == "__main__":
    from sympy import symbols, diff, lambdify

    expr_str = input("Enter the function (in terms of x, e.g. x**3 - 4*x - 9): ")
    x = symbols('x')

    expr = eval(expr_str)
    derivative = diff(expr, x)

    f = lambdify(x, expr)  
    df = lambdify(x, derivative)  

    x0 = float(input("Enter initial guess: "))

    try:
        root = newton_raphson(f, df, x0)
        print(f"Root found: {root:.6f}")
    except ValueError as e:
        print(e)
        
# Output

# Enter the function (in terms of x, e.g. x**3 - 4*x - 9): x**3 + 2*x - 2
# Enter initial guess: 1
# Root found: 0.770917