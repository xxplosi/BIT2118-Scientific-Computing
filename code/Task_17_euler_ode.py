import numpy as np
import matplotlib.pyplot as plt

# Newton's law of cooling
ambient = 25.0
initial_temp = 90.0
k = 0.12
step = 1.0
end_time = 30.0

def cooling_rate(T):
    return -k * (T - ambient)

time = np.arange(0, end_time + step, step)
temperature = np.zeros_like(time)
temperature[0] = initial_temp

for i in range(len(time) - 1):
    temperature[i + 1] = (
        temperature[i] + step * cooling_rate(temperature[i])
    )

exact = ambient + (initial_temp - ambient) * np.exp(-k * time)

print("BIT 2118 - Task 17: Euler Method")
print(f"Euler temperature after 30 minutes: {temperature[-1]:.2f} °C")
print(f"Exact temperature after 30 minutes: {exact[-1]:.2f} °C")
print(f"Absolute error: {abs(temperature[-1] - exact[-1]):.4f} °C")

# Parameter change: reduce the step size to 0.5 minutes
step2 = 0.5
time2 = np.arange(0, end_time + step2, step2)
temperature2 = np.zeros_like(time2)
temperature2[0] = initial_temp

for i in range(len(time2) - 1):
    temperature2[i + 1] = (
        temperature2[i]
        + step2 * cooling_rate(temperature2[i])
    )

print("Euler result with 0.5-minute steps:",
      f"{temperature2[-1]:.2f} °C")

plt.plot(time, temperature, marker=".", label="Euler, step=1")
plt.plot(time2, temperature2, label="Euler, step=0.5")
plt.plot(time, exact, "--", label="Exact solution")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (°C)")
plt.title("Cooling of a Hot Object")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("results/Task_17_euler.png")
plt.show()