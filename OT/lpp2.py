from scipy.optimize import linprog

def farmer():
    print("Enter total acres available:")
    acres = int(input())

    print("Enter minimum acres for wheat and barley (space-separated):")
    min_acres = list(map(int, input().split()))

    print("Enter fertilizer and insecticide available (space-separated):")
    resources = list(map(int, input().split()))

    print("Enter fertilizer per acre (wheat, barley):")
    fert_req = list(map(int, input().split()))

    print("Enter insecticide per acre (wheat, barley):")
    insect_req = list(map(int, input().split()))

    print("Enter profit per acre (wheat, barley):")
    profit = list(map(int, input().split()))

    c = [-profit[0], -profit[1]]  # Negative for maximization
    A = [
        [fert_req[0], fert_req[1]],  # Fertilizer constraint
        [insect_req[0], insect_req[1]]  # Insecticide constraint
    ]
    b = [resources[0], resources[1]]
    bounds = [(min_acres[0], None), (min_acres[1], None)]

    result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    wheat, barley = result.x
    max_profit = -result.fun

    print(f"\nOptimal wheat acres: {wheat:.0f}, Optimal barley acres: {barley:.0f}")
    print(f"Maximum profit: ${max_profit:.2f}")

farmer()
