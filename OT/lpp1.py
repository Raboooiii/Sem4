from scipy.optimize import linprog

def furniture():
    print("Enter available wood units:")
    wood = int(input())

    print("Enter available metal units:")
    metal = int(input())

    print("Enter wood required per chair and per table (space-separated):")
    wood_req = list(map(int, input().split()))

    print("Enter metal required per chair and per table (space-separated):")
    metal_req = list(map(int, input().split()))

    print("Enter profit per chair and per table (space-separated):")
    profit = list(map(int, input().split()))

    c = [-profit[0], -profit[1]]  # Negative for maximization
    A = [
        [wood_req[0], wood_req[1]],  # Wood constraint
        [metal_req[0], metal_req[1]]  # Metal constraint
    ]
    b = [wood, metal]

    result = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None), (0, None)], method='highs')

    chairs, tables = result.x
    max_profit = -result.fun

    print(f"\nOptimal chairs: {chairs:.0f}, Optimal tables: {tables:.0f}")
    print(f"Maximum profit: ${max_profit:.2f}")

furniture()
