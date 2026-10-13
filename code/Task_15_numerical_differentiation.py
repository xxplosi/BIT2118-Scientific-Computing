import numpy as np
import matplotlib.pyplot as plt

time = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
position = np.array([0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0])

speed = np.zeros_like(position)

# Forward difference at the beginning
speed[0] = (position[1] - position[0]) / (time[1] - time[0])

# Central differences for interior measurements
for i in range(1, len(time) - 1):
    speed[i] = (
        (position[i + 1] - position[i - 1])
        / (time[i + 1] - time[i - 1])
    )

# Backward difference at the end
speed[-1] = (
    (position[-1] - position[-2])
    / (time[-1] - time[-2])
)

print("BIT 2118 - Task 15: Numerical Differentiation")

for t, p, v in zip(time, position, speed):
    print(f"Time={t:.0f}s, Position={p:.1f}m, Speed={v:.2f}m/s")

# Parameter change: compare the speed at 2 seconds
# using a two-second central interval versus a one-sided interval
central_speed = (position[3] - position[1]) / (time[3] - time[1])
forward_speed = (position[3] - position[2]) / (time[3] - time[2])

print("\nSpeed estimate at 2 seconds using the wider interval:",
      f"{central_speed:.2f} m/s")
print("Speed estimate from the next one-second interval:",
      f"{forward_speed:.2f} m/s")

plt.plot(time, speed, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Estimated speed (m/s)")
plt.title("Speed Estimated from GPS Position")
plt.grid(True)
plt.tight_layout()
plt.savefig("results/Task_15_differentiation.png")
plt.show()