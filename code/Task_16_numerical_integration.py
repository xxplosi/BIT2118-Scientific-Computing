import numpy as np
from scipy.integrate import simpson

# Power readings in kW at two-hour intervals
time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
power_kw = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])

# Integrate power over time to estimate energy
energy_trapezoid = np.trapezoid(power_kw, x=time_hours)
energy_simpson = simpson(power_kw, x=time_hours)

print("BIT 2118 - Task 16: Numerical Integration")
print(f"Trapezoidal energy: {energy_trapezoid:.3f} kWh")
print(f"Simpson energy: {energy_simpson:.3f} kWh")
print(f"Difference: {abs(energy_simpson - energy_trapezoid):.3f} kWh")

# Parameter change: increase every power reading by 10%
power_changed = power_kw * 1.10

print("\nAfter increasing power readings by 10%:")
print("New trapezoidal energy:",
      f"{np.trapezoid(power_changed, x=time_hours):.3f} kWh")
print("New Simpson energy:",
      f"{simpson(power_changed, x=time_hours):.3f} kWh")