import numpy as np
from scipy.optimize import linear_sum_assignment

def assignment_problem():
    print("\nAssignment Problem Solver (Hungarian Algorithm)")
    print("---------------------------------------------")
    
    n = int(input("Enter number of workers/jobs: "))
    
    print("\nEnter cost matrix (row = workers, column = jobs):")
    cost_matrix = []
    for i in range(n):
        row = list(map(float, input(f"Costs for worker {i+1} (space-separated): ").split()))
        cost_matrix.append(row)
    cost_matrix = np.array(cost_matrix)
    
    # Solve using Hungarian Algorithm
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    total_cost = cost_matrix[row_ind, col_ind].sum()
    
    print("\nOptimal Assignments:")
    for worker, job in zip(row_ind, col_ind):
        print(f"Worker {worker+1} → Job {job+1} (Cost: {cost_matrix[worker][job]:.2f})")
    print(f"Total Minimum Cost: {total_cost:.2f}")

assignment_problem()
