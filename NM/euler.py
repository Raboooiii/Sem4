def eulers_method():
    
    print("\nEULER’S METHOD FOR ORDINARY DIFFERENTIAL EQUATIONS")
    print("-----------------------------------------------")
    print("Enter the differential equation in terms of x and y (e.g., x + y):")
    ode_str = input("dy/dx = ")
    
    def dy_dx(x, y):
        return eval(ode_str)
    
    x0 = float(input("\nEnter initial x value (x): "))
    y0 = float(input("Enter initial y value (y): "))
    h = float(input("Enter step size (h): "))
    n = int(input("Enter number of steps: "))
    x = x0
    y = y0
    
    for i in range(1, n+1):
        y += h * dy_dx(x, y)
        x += h
    print(f"\nFinal solution at x = {x:.6f} is y = {y:.6f}")
    
if __name__ == "__main__":
    eulers_method()
