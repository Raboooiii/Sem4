import math

def eoq():
    print("\nEconomic Order Quantity (EOQ) Calculator")
    print("---------------------------------------")
    
    A = float(input("Enter annual demand (units): "))
    B = float(input("Enter ordering cost per order ($): "))
    C = float(input("Enter holding cost per unit/year ($): "))

    q = math.sqrt((2 * A * B) / C)
    orders_per_year = A / q
    total_cost = (A * B / q) + (C * q / 2)

    print("\nResults:")
    print(f"Optimal Order Quantity (EOQ): {q:.2f} units")
    print(f"Number of Orders/Year: {orders_per_year:.2f}")
    print(f"Total Annual Inventory Cost: ${total_cost:.2f}")

eoq()
