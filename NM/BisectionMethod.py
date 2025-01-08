def bisection_method(f, a, b, tol):
    if f(a) * f(b) > 0:
        print("The function must have opposite sign.")
        return None
    while (b - a) / 2 > tol:
        m = (a + b) / 2  
        if f(m) == 0:
            return m  
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m

    return (a + b) / 2

if __name__ == "__main__":
    print("Bisection Method to find a root of f(x) = 0.")

    user_function = input("Enter f(x) (e.g., x**3 - x - 2): ")
    exec(f"global f\ndef f(x): return {user_function}")

    a = float(input("Enter the left endpoint (a): "))
    b = float(input("Enter the right endpoint (b): "))
    tol = float(input("Enter the tolerance (e.g., 1e-6): "))

    try:
        root = bisection_method(f, a, b, tol) 
        decimal_places = abs(int(f"{tol:e}".split('e')[-1]))
        print(f"Approximate root: {root:.{decimal_places}f}")
    except Exception as e:
        print(f"Error: {e}")

#Output

#Bisection Method to find a root of f(x) = 0.
#Enter f(x) (e.g., x**3 - x - 2): x+1
#Enter the left endpoint (a): 0
#Enter the right endpoint (b): 3
#Enter the tolerance (e.g., 1e-6): 1e-6
#Approximate root: 2.999999