import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar

def heat_balance(T):
    return T - 25 - 10 * np.exp(-T / 20)

solution = root_scalar(
    heat_balance,
    bracket=[20, 40],
    method="bisect",
    xtol=1e-10
)

def g(T):
    return 25 + 10 * np.exp(-T / 20)

T = 30.0
history = [T]

for _ in range(1000):
    T_new = g(T)
    history.append(T_new)

    if abs(T_new - T) < 1e-10:
        break

    T = T_new

print("BIT 2118 - Task 10: Root Finding")
print(f"Bisection root: {solution.root:.6f} °C")
print(f"Fixed-point root: {history[-1]:.6f} °C")
print("Fixed-point iterations:", len(history) - 1)

# Parameter change: increase the base temperature from 25 to 27
def changed_balance(T):
    return T - 27 - 10 * np.exp(-T / 20)

changed = root_scalar(
    changed_balance,
    bracket=[20, 40],
    method="bisect"
)

print(f"Root after parameter change: {changed.root:.6f} °C")

temps = np.linspace(20, 40, 300)
plt.plot(temps, heat_balance(temps), label="Heat balance")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(solution.root, linestyle="--", label="Root")
plt.xlabel("Temperature (°C)")
plt.ylabel("Heat-balance function")
plt.title("Equilibrium Temperature")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("results/Task_10_root.png")
plt.show()