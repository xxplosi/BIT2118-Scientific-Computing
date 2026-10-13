import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

capacity = 1000.0
mean_demand = 850.0
std_demand = 120.0
N = 100_000

# Simulate uncertain demand
demand = rng.normal(mean_demand, std_demand, N)
overloaded = demand > capacity
probability = overloaded.mean()

print("BIT 2118 - Task 20: Monte Carlo Simulation")
print(f"Simulations: {N}")
print(f"Overload cases: {overloaded.sum()}")
print(f"Estimated overload probability: {probability:.4%}")

# Calculate running probability
running_probability = (
    np.cumsum(overloaded) / np.arange(1, N + 1)
)

indices = np.unique(
    np.logspace(1, np.log10(N), 200).astype(int)
) - 1

plt.semilogx(
    indices + 1,
    running_probability[indices],
    label="Estimated probability"
)

plt.axhline(probability, linestyle="--", label="Final estimate")
plt.xlabel("Number of simulations")
plt.ylabel("Estimated overload probability")
plt.title("Monte Carlo Estimate of Server Overload Risk")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("results/Task_20_monte_carlo.png")
plt.show()

# Parameter change: increase the simulation count to one million
N2 = 1_000_000
demand2 = rng.normal(mean_demand, std_demand, N2)
probability2 = np.mean(demand2 > capacity)

print("\nAfter increasing simulations to one million:")
print(f"Estimated overload probability: {probability2:.4%}")