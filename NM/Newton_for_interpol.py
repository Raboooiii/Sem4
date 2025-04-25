def newton_forward_interpolation():
    print("\nNEWTON’S FORWARD INTERPOLATION METHOD")
    print("-----------------------------------")
    
    n = int(input("Enter the number of data points: "))
    x = []
    y = []
    print("\nEnter the data points (x, y):")
    for i in range(n):
        x_val = float(input(f"x[{i}]: "))
        y_val = float(input(f"y[{i}]: "))
        x.append(x_val)
        y.append(y_val)
    diff_table = [[0] * n for _ in range(n)]
    for i in range(n):
        diff_table[i][0] = y[i]
        
    for j in range(1, n):
        for i in range(n- j):
            diff_table[i][j] = diff_table[i+1][j-1]- diff_table[i][j-1]
    print("\nForward Difference Table:")
    print("x\t\ty", end="")
    for i in range(1, n):
        print(f"\t\t^{i}y", end="")
    print()
    
    for i in range(n):
        print(f"{x[i]:.4f}", end="\t")
        for j in range(n- i):
            print(f"{diff_table[i][j]:.4f}", end="\t\t")
        print()
    x_target = float(input("\nEnter the point for interpolation: "))
    h = x[1]- x[0]
    u = (x_target- x[0]) / h
    result = diff_table[0][0]
    fact = 1
    u_term = 1
    print("\nInterpolation Calculation:")
    print(f"Initial result = {result:.6f}")
    for i in range(1, n):
        fact *= i
        u_term *= (u- (i- 1))
        term = (u_term * diff_table[0][i]) / fact
        result += term
    print(f"\nInterpolated value at x = {x_target:.4f} is {result:.6f}")
newton_forward_interpolation()
