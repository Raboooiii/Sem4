import numpy as np

def gauss_elimination_pivoting():

    print("\nGAUSSIAN ELIMINATION WITH PARTIAL PIVOTING")
    print("----------------------------------------")
    
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
    
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    for i in range(n):
        max_row = i + np.argmax(np.abs(Ab[i:, i]))
        if max_row != i:
            Ab[[i, max_row]] = Ab[[max_row, i]]
        
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]
    
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
    
    print("\nFinal solution:")
    for i in range(n):
        print(f"x[{i+1}] = {x[i]:.6f}")

gauss_elimination_pivoting()
