import numpy as np
from scipy.optimize import minimize

# x = Type A capacity units
# y = Type B capacity units
# Cost per unit: A = 12, B = 18
# Capacity per unit: A = 100, B = 170

def cost(z):
    x, y = z
    return 12 * x + 18 * y

def capacity_constraint(z):
    x, y = z
    return 100 * x + 170 * y - 1000

solution = minimize(
    cost,
    x0=[5, 3],
    method="SLSQP",
    bounds=[(0, None), (0, None)],
    constraints={"type": "ineq", "fun": capacity_constraint}
)

print("BIT 2118 - Task 19: Optimization")
print("Optimization success:", solution.success)
print("Type A allocation:", solution.x[0])
print("Type B allocation:", solution.x[1])
print("Capacity:", 100 * solution.x[0] + 170 * solution.x[1])
print("Planning cost:", solution.fun)

# Parameter change: increase required capacity from 1000 to 1200
def changed_capacity(z):
    x, y = z
    return 100 * x + 170 * y - 1200

changed = minimize(
    cost,
    x0=[5, 4],
    method="SLSQP",
    bounds=[(0, None), (0, None)],
    constraints={"type": "ineq", "fun": changed_capacity}
)

print("\nAfter increasing required capacity to 1200:")
print("Type A allocation:", changed.x[0])
print("Type B allocation:", changed.x[1])
print("Capacity:", 100 * changed.x[0] + 170 * changed.x[1])
print("Planning cost:", changed.fun)

# Whole-unit solution: search integer combinations
for required in [1000, 1200]:
    best = None

    for a in range(0, 30):
        for b in range(0, 30):
            capacity = 100 * a + 170 * b

            if capacity >= required:
                total_cost = 12 * a + 18 * b

                if best is None or total_cost < best[0]:
                    best = (total_cost, a, b, capacity)

    print(f"Best whole-unit plan for {required} capacity:", best)