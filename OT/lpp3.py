from scipy.optimize import linprog

def bakery():
    print("Enter daily budget:")
    budget = int(input())

    print("Enter max cakes per day:")
    max_cakes = int(input())

    print("Enter demand for chocolate and vanilla cakes (space-separated):")
    demand = list(map(int, input().split()))

    print("Enter cost to make (chocolate, vanilla):")
    cost = list(map(int, input().split()))

    print("Enter selling price (chocolate, vanilla):")
    price = list(map(int, input().split()))

    c = [-price[0], -price[1]]  # Negative for maximization
    A = [
        [cost[0], cost[1]],  # Budget constraint
        [1, 1]  # Production constraint
    ]
    b = [budget, max_cakes]
    bounds = [(demand[0], None), (demand[1], None)]

    result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    chocolate, vanilla = result.x
    max_revenue = -result.fun

    print(f"\nOptimal chocolate cakes: {chocolate:.0f}, Optimal vanilla cakes: {vanilla:.0f}")
    print(f"Maximum revenue: ${max_revenue:.2f}")

bakery()
