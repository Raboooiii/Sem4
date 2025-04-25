def knapsack():
    print("Enter the number of items:")
    n = int(input())

    print("Enter the weights of items (space-separated):")
    weights = list(map(int, input().split()))

    print("Enter the values of items (space-separated):")
    values = list(map(int, input().split()))

    print("Enter the knapsack capacity:")
    capacity = int(input())

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    print("\nMaximum value in knapsack:", dp[n][capacity])

knapsack()
