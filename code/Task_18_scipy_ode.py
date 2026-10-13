import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# RC circuit charging model
supply_voltage = 5.0
resistance = 1000.0
capacitance = 0.001
initial_voltage = 0.0

def rc_circuit(t, V):
    return [(supply_voltage - V[0]) / (resistance * capacitance)]

times = np.linspace(0, 5, 200)

solution = solve_ivp(
    rc_circuit,
    (0, 5),
    [initial_voltage],
    t_eval=times,
    rtol=1e-9,
    atol=1e-11
)

exact = supply_voltage * (
    1 - np.exp(-solution.t / (resistance * capacitance))
)

print("BIT 2118 - Task 18: SciPy ODE Solver")
print("Solver success:", solution.success)
print(f"Voltage at 5 seconds: {solution.y[0, -1]:.4f} V")
print("Maximum error:",
      f"{np.max(np.abs(solution.y[0] - exact)):.3e} V")

# Parameter change: double the capacitance
capacitance2 = 0.002

def changed_circuit(t, V):
    return [(supply_voltage - V[0]) / (resistance * capacitance2)]

changed = solve_ivp(
    changed_circuit, (0, 5), [initial_voltage],
    t_eval=times
)

print("Voltage after doubling capacitance:",
      f"{changed.y[0, -1]:.4f} V")

plt.plot(solution.t, solution.y[0], label="Original circuit")
plt.plot(changed.t, changed.y[0], label="Double capacitance")
plt.plot(solution.t, exact, "--", label="Exact original")
plt.xlabel("Time (s)")
plt.ylabel("Capacitor voltage (V)")
plt.title("RC Circuit Charging")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("results/Task_18_scipy_ode.png")
plt.show()