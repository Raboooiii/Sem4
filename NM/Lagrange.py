def lagrange_interpolation():
    print("\nLAGRANGE INTERPOLATION METHOD")
    print("---------------------------")
    n = int(input("Enter the number of data points: "))
    x = []
    y = []
    print("\nEnter the data points (x, y):")
    for i in range(n):
        x_val = float(input(f"x[{i}]: "))
        y_val = float(input(f"y[{i}]: "))
        x.append(x_val)
        y.append(y_val)
        
    x_target = float(input("\nEnter the point for interpolation: "))
    result = 0.0
    print("\nCalculating Lagrange polynomial terms:")
    
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                # Calculate the Lagrange basis polynomial
                numerator = x_target- x[j]
                denominator = x[i]- x[j]
                factor = numerator / denominator
                term *= factor
                
        result += term
        
    print(f"\nInterpolated value at x = {x_target:.4f} is {result:.6f}")
    
if __name__ == "__main__":   
    print("Lagrange Interpolation Program")
    lagrange_interpolation()
