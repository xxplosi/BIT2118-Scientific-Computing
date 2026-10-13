import numpy as np
from scipy.optimize import root

# Circle: x² + y² = radius²
# Parabola: y = x² - 1

def equations(z, radius=2.0):
    x, y = z
    return [
        x**2 + y**2 - radius**2,
        y - (x**2 - 1)
    ]

print("BIT 2118 - Task 12: Nonlinear Equations")

for guess in ([1.0, 1.0], [-1.0, 1.0]):
    solution = root(equations, guess)
    print("\nInitial guess:", guess)
    print("Intersection:", np.round(solution.x, 6))
    print("Residuals:", equations(solution.x))
    print("Converged:", solution.success)

# Parameter change: increase circle radius from 2 to 2.5
print("\nAfter increasing the circle radius to 2.5:")

for guess in ([1.0, 1.0], [-1.0, 1.0]):
    solution = root(
        lambda z: equations(z, radius=2.5),
        guess
    )
    print("Intersection:", np.round(solution.x, 6))
    print("Converged:", solution.success)