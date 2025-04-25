import numpy as np

def gauss_seidel():

    print("\nGAUSS-SEIDEL ITERATIVE METHOD")
    print("---------------------------")
    
    n = int(input("Enter the size of the system (n): "))
    
    A = np.zeros((n, n))
    b = np.zeros(n)
    
    print("\nEnter the coefficient matrix A:")
    for i in range(n):
        for j in range(n):
            A[i, j] = float(input(f"A[{i+1}][{j+1}]: "))
    
    print("\nEnter the right-hand side vector b:")
    for i in range(n):
        b[i] = float(input(f"b[{i+1}]: "))
    
    x0 = np.zeros(n)
    print("\nEnter initial guess (press Enter for default zeros):")
    for i in range(n):
        val = input(f"x0[{i+1}]: ")
        x0[i] = float(val) if val else 0.0
    
    tol = float(input("\nEnter tolerance (default 1e-6): ") or "1e-6")
    max_iter = int(input("Enter maximum iterations (default 1000): ") or "1000")
    
    x = x0.copy()
    print("\nIteration process:")
    
    for iteration in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i+1:], x_old[i+1:])
            x[i] = (b[i] - sum1 - sum2) / A[i, i]
        
        print(f"Iteration {iteration + 1}: {x}")
        
        if np.linalg.norm(x - x_old) < tol:
            print(f"\nConverged after {iteration + 1} iterations")
            break
    
    print("\nFinal solution:")
    for i in range(n):
        print(f"x[{i+1}] = {x[i]:.6f}")

gauss_seidel()
