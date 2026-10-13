import numpy as np

# Type A servers: 4 CPU units and 8 GB memory
# Type B servers: 2 CPU units and 12 GB memory
A = np.array([
    [4.0, 2.0],
    [8.0, 12.0]
])

# Total CPU = 20; total memory = 72 GB
b = np.array([20.0, 72.0])

solution = np.linalg.solve(A, b)
residual = b - A @ solution

print("BIT 2118 - Task 6: Linear Systems")
print(f"Type A server units: {solution[0]:.2f}")
print(f"Type B server units: {solution[1]:.2f}")
print("Reconstructed totals:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))

# Parameter change: increase total CPU from 20 to 24
b_changed = np.array([24.0, 72.0])
solution_changed = np.linalg.solve(A, b_changed)

print("\nAfter increasing total CPU to 24:")
print("New solution:", solution_changed)
print("New reconstructed totals:", A @ solution_changed)