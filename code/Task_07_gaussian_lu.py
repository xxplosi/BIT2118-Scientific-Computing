import numpy as np
from scipy.linalg import lu_factor, lu_solve

A = np.array([
    [4.0, -1.0, 0.0],
    [-1.0, 4.0, -1.0],
    [0.0, -1.0, 3.0]
])

measurement_sets = [
    np.array([15.0, 10.0, 10.0]),
    np.array([16.0, 11.0, 9.0]),
    np.array([14.0, 12.0, 11.0])
]

# Factor the coefficient matrix once
lu, piv = lu_factor(A)

print("BIT 2118 - Task 7: LU Decomposition")

for i, b in enumerate(measurement_sets, start=1):
    x = lu_solve((lu, piv), b)
    residual = b - A @ x

    print(f"\nMeasurement set {i}")
    print("Solution:", np.round(x, 4))
    print("Residual norm:", np.linalg.norm(residual))

# Parameter change: increase the first measurement
b_changed = measurement_sets[0].copy()
b_changed[0] += 2

changed_solution = lu_solve((lu, piv), b_changed)
print("\nAfter increasing the first measurement by 2:")
print("New solution:", np.round(changed_solution, 4))