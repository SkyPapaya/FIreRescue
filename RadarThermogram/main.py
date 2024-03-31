import numpy as np
import matplotlib.pyplot as plt

temperature_matrix = np.array([
    [0, 1, 100, 100, 100, 1, 100, 100, 100, 100],
    [100, 1, 100, 100, 100, 1, 100, 100, 100, 100],
    [100, 1, 100, 1, 100, 1, 100, 100, 100, 100],
    [100, 1, 100, 1, 100, 1, 100, 100, 100, 100],
    [100, 1, 100, 1, 100, 100, 100, 100, 100, 100],
    [100, 1, 100, 1, 1, 1, 1, 1, 1, 1],
    [100, 1, 1, 1, 100, 100, 100, 100, 100, 100],
    [100, 1, 100, 100, 100, 100, 100, 100, 100, 100],
    [100, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [100, 100, 100, 100, 1, 100, 100, 100, 100, 100]
], dtype=float)


def dfs(matrix, x, y):
    rows, cols = matrix.shape
    # Check if the current position is out of bounds or not 1
    if x < 0 or x >= rows or y < 0 or y >= cols or matrix[x, y] != 1:
        return False
    # Check if it reached the edge
    if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
        matrix[x, y] = 1000
        return True
    # Replace the value with 1000
    matrix[x, y] = 1000
    # Explore in all four directions
    if (dfs(matrix, x + 1, y) or
            dfs(matrix, x - 1, y) or
            dfs(matrix, x, y + 1) or
            dfs(matrix, x, y - 1)):
        return True
    return False


# Start DFS from (1, 1)
dfs(temperature_matrix, 1, 1)

plt.figure(figsize=(8, 6))
plt.imshow(temperature_matrix, cmap='hot', interpolation='nearest')
plt.colorbar(label='Temperature')
plt.title('Temperature Heatmap with Path Colored as 1000')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
# print(temperature_matrix)
