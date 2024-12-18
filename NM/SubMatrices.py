def SubMatrices(m1, m2, rows, cols):
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = m1[i][j] - m2[i][j]
    return result

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("Enter the elements of the first matrix:")
m1 = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Element [{i}][{j}]: ")))
    m1.append(row)

print("Enter the elements of the second matrix:")
m2 = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Element [{i}][{j}]: ")))
    m2.append(row)

result = SubMatrices(m1, m2, rows, cols)

print("Difference of matrices:")
for row in result:
    print(row)
