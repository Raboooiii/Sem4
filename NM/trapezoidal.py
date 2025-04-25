def trapezoidal_rule():
    print("\nTRAPEZOIDAL RULE FOR NUMERICAL INTEGRATION")
    print("----------------------------------------")
    print("Enter the function to integrate in terms of x (e.g., x**2 + 3*x + 2):")
    func_str = input("f(x) = ")
    
    def f(x):
        return eval(func_str)
    a = float(input("\nEnter lower limit of integration (a): "))
    b = float(input("Enter upper limit of integration (b): "))
    n = int(input("Enter number of subintervals (n): "))
    h = (b- a) / n
    sum_fx = f(a) + f(b)
    for i in range(1, n):
        x_i = a + i * h
        fx_i = f(x_i)
        sum_fx += 2 * fx_i
    integral = (h / 2) * sum_fx
    print("\nIntegral calculation:")
    print(f"Sum of function values = {sum_fx:.6f}")
    print(f"Step size (h) = {h:.6f}")
    
    print(f"Integral (h/2) × sum = ({h:.6f}/2) × {sum_fx:.6f} = {integral:.6f}")
if __name__ == "__main__":
    trapezoidal_rule()
