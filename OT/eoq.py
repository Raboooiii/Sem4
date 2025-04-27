import math

def eoq():
    print("\nEconomic Order Quantity (EOQ) Calculator")
    print("---------------------------------------")
    
    demand = float(input("Enter annual demand (units): "))
    setup_cost = float(input("Enter ordering cost per order ($): "))
    holding_cost = float(input("Enter holding cost per unit/year ($): "))

    q = math.sqrt((2 * demand * setup_cost) / holding_cost)
    orders_per_year = demand / q
    total_cost = (demand * setup_cost / q) + (holding_cost * q / 2)

    print("\nResults:")
    print(f"Optimal Order Quantity (EOQ): {q:.2f} units")
    print(f"Number of Orders/Year: {orders_per_year:.2f}")
    print(f"Total Annual Inventory Cost: ${total_cost:.2f}")

eoq()
