import numpy as np

# Demonstrate floating-point representation errors
calculated = 0.1 + 0.2
expected = 0.3

print("BIT 2118 - Task 4: Numerical Errors")
print("0.1 + 0.2 =", calculated)
print("Exact comparison:", calculated == expected)
print("Tolerance comparison:", np.isclose(calculated, expected))

# Absolute and relative errors
true_value = np.sqrt(2)
approx_value = 1.414

absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)

print(f"True value of sqrt(2): {true_value:.10f}")
print(f"Approximation: {approx_value}")
print(f"Absolute error: {absolute_error:.8f}")
print(f"Relative error: {relative_error:.8%}")

# Compare direct and numerically stable formulas
for x in [1e-4, 1e-8, 1e-12]:
    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)
    print(f"x={x:.0e}: direct={direct:.10f}, stable={stable:.10f}")

# Parameter change: use a more accurate approximation
approx_value = 1.4142135
print("\nAfter improving the approximation:")
print("New absolute error:", abs(true_value - approx_value))