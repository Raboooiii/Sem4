import numpy as np

def transportation_problem():
    print("\nTransportation Problem Solver (Northwest Corner Rule)")
    print("---------------------------------------------------")
    
    m = int(input("Enter number of supply sources: "))
    n = int(input("Enter number of demand destinations: "))
    
    print("\nEnter transportation costs matrix (row-wise):")
    cost_matrix = []
    for i in range(m):
        row = list(map(float, input(f"Costs for source {i+1} (space-separated): ").split()))
        cost_matrix.append(row)
    cost_matrix = np.array(cost_matrix)
    
    supply = list(map(float, input("\nEnter supply capacities (space-separated): ").split()))
    demand = list(map(float, input("Enter demand requirements (space-separated): ").split()))
    
    allocation = np.zeros((m, n))
    total_cost = 0
    i, j = 0, 0
    
    while i < m and j < n:
        quantity = min(supply[i], demand[j])
        allocation[i][j] = quantity
        supply[i] -= quantity
        demand[j] -= quantity
        total_cost += quantity * cost_matrix[i][j]
        
        if supply[i] == 0:
            i += 1
        else:
            j += 1
    
    print("\nOptimal Allocation Matrix:")
    print(allocation)
    print(f"Total Transportation Cost: {total_cost:.2f}")
    
transportation_problem()
