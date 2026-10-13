import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
response_ms = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)

def model(x, a, b, c):
    return a * x**2 + b * x + c

parameters, covariance = curve_fit(model, users, response_ms)
a, b, c = parameters

predicted = model(users, a, b, c)
rmse = np.sqrt(np.mean((response_ms - predicted)**2))

print("BIT 2118 - Task 14: Curve Fitting")
print(f"Model: y = {a:.6f}x² + {b:.4f}x + {c:.2f}")
print(f"RMSE: {rmse:.2f} ms")
print(f"Prediction at 400 users: {model(400, *parameters):.2f} ms")

# Parameter change: predict for 300 users instead of 400
print(f"Prediction at 300 users: {model(300, *parameters):.2f} ms")

x_plot = np.linspace(users.min(), 400, 300)
plt.scatter(users, response_ms, label="Measured data")
plt.plot(x_plot, model(x_plot, *parameters), label="Quadratic fit")
plt.xlabel("Concurrent users")
plt.ylabel("Response time (ms)")
plt.title("Server Response-Time Curve Fitting")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("results/Task_14_curve_fitting.png")
plt.show()