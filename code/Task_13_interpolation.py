import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline

hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
temperature = np.array([18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0])

linear = interp1d(hours, temperature, kind="linear")
cubic = CubicSpline(hours, temperature)

times = np.arange(8, 14.001, 1/6)

linear_values = linear(times)
cubic_values = cubic(times)

print("BIT 2118 - Task 13: Interpolation")
print(f"Linear estimate at 10:30: {float(linear(10.5)):.2f} °C")
print(f"Cubic estimate at 10:30: {float(cubic(10.5)):.2f} °C")

# Parameter change: estimate at 10:45 instead
print(f"Linear estimate at 10:45: {float(linear(10.75)):.2f} °C")
print(f"Cubic estimate at 10:45: {float(cubic(10.75)):.2f} °C")

plt.scatter(hours, temperature, label="Measurements")
plt.plot(times, linear_values, label="Linear")
plt.plot(times, cubic_values, label="Cubic spline")
plt.xlabel("Hour")
plt.ylabel("Temperature (°C)")
plt.title("Hourly Temperature Interpolation")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("results/Task_13_interpolation.png")
plt.show()