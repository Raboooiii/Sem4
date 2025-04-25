import numpy as np

def gauss_jordan():

    print("\nGAUSS-JORDAN ELIMINATION METHOD")
    print("-----------------------------")
    
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
    
    print("\nStarting augmented matrix:")
    print(Ab)
    
    for i in range(n):
        max_row = i + np.argmax(np.abs(Ab[i:, i]))
        if max_row != i:
            Ab[[i, max_row]] = Ab[[max_row, i]]
            print(f"\nSwapped row {i+1} with row {max_row+1}")
            print(Ab)
            
        pivot = Ab[i, i]
        Ab[i] = Ab[i] / pivot
        print(f"\nNormalized row {i+1} by dividing by {pivot:.2f}")
        print(Ab)
        
        for j in range(n):
            if j != i and Ab[j, i] != 0:
                factor = Ab[j, i]
                Ab[j] -= factor * Ab[i]
                print(f"\nEliminated row {j+1} using row {i+1}")
                print(Ab)
    
    x = Ab[:, -1]
    
    print("\nFinal solution:")
    for i in range(n):
        print(f"x[{i+1}] = {x[i]:.6f}")

gauss_jordan()
