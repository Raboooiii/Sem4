def false_position(f,a,b,tol = 1e-6, max_Iter=100):
    if f(a) * f(b) > 0:
        print("f(a) and f(b) should have different symbols")
        return None, 0
    
    iter_count = 0
    c = a

    while iter_count < max_Iter:
        c = (a*f(b) - b*f(a))/ (f(b) - f(a))

        if abs(f(c)) < tol:
            return c, iter_count
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        iter_count += 1

    print(f"Max no. of iterations reached. Current root estimate: {c}")
    return c, iter_count

if __name__ == "__main__":

    func_str = input("Enter the function f(x) (use 'x' as the variable): ")
    a = float(input("Enter the start of the interval a: "))
    b = float(input("Enter the end of the interval b: "))
    tol = float(input("Enter the desired tolerance (default 1e-6): ") or 1e-6)
    max_iter = int(input("Enter the maximum number of iterations (default 100): ") or 100)
    
    def f(x):
        return eval(func_str)
    
    root, iterations = false_position(f, a, b, tol, max_iter)
    
    if root is not None:
        print(f"Root found: {root:.6f} after {iterations} iterations")
