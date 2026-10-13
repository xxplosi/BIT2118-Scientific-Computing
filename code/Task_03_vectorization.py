import numpy as np
import timeit

# BIT 2118 - Task 3: Mathematical Functions and Vectorization
# Real-world application: Network latency analysis

# Input: Simulate one million network latency readings in milliseconds
rng = np.random.default_rng(42)
latency_ms = rng.uniform(5, 250, 1_000_000)

# Method 1: Traditional Python loop
def loop_version():
    squared = []
    for value in latency_ms:
        seconds = value / 1000.0
        squared.append(seconds ** 2)
    return squared

# Method 2: NumPy vectorization
def vectorized_version():
    seconds = latency_ms / 1000.0
    return seconds ** 2

# Measure execution time
loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3

# Calculate the vectorized result
result = vectorized_version()

print("BIT 2118 - Task 3: Vectorization")
print("-" * 40)
print("Number of latency readings:", len(latency_ms))
print("First five latency readings (ms):", np.round(latency_ms[:5], 3))
print("First five squared latency values (s²):",
      np.round(result[:5], 8))
print(f"Python loop time: {loop_time:.4f} seconds")
print(f"NumPy vectorized time: {vector_time:.4f} seconds")

if vector_time > 0:
    print(f"Approximate speed-up: {loop_time / vector_time:.2f}x")

# Parameter change: process only 100,000 readings
smaller_data = latency_ms[:100_000]

def smaller_vectorized_version():
    seconds = smaller_data / 1000.0
    return seconds ** 2

smaller_time = timeit.timeit(smaller_vectorized_version, number=3) / 3

print("\nParameter change: 100,000 readings instead of 1,000,000")
print("Number of readings:", len(smaller_data))
print(f"Average vectorized time: {smaller_time:.6f} seconds")