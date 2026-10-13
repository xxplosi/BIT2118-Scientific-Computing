import numpy as np

# BIT 2118: Task 2 - NumPy Arrays and Numerical Computation
# Real-world application: Weather station temperature analysis

# Input: 24 hourly temperature readings in degrees Celsius
temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])

# Mathematical operations
mean_temp = np.mean(temperatures_c)
min_temp = np.min(temperatures_c)
max_temp = np.max(temperatures_c)

# Vectorized conversion from Celsius to Fahrenheit
temperatures_f = 1.8 * temperatures_c + 32

# Display results
print("BIT 2118 - Task 2: NumPy Arrays")
print("-" * 40)
print(f"Number of readings: {len(temperatures_c)}")
print(f"Daily mean temperature: {mean_temp:.2f} °C")
print(f"Minimum temperature: {min_temp:.2f} °C")
print(f"Maximum temperature: {max_temp:.2f} °C")
print("First six Fahrenheit readings:", np.round(temperatures_f[:6], 2))

# Parameter change: increase every reading by 2 °C
modified_temperatures = temperatures_c + 2

print("\nAfter increasing all readings by 2 °C:")
print(f"New mean: {np.mean(modified_temperatures):.2f} °C")
print(f"New minimum: {np.min(modified_temperatures):.2f} °C")
print(f"New maximum: {np.max(modified_temperatures):.2f} °C")