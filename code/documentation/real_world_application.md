Related Real-World Application: Smart-Meter Electricity Analysis
1. Problem Statement

A household wants to estimate its electrical energy consumption from power measurements collected at regular intervals.

2. Assumptions
Power measurements are recorded every two hours.
Power changes approximately linearly between consecutive measurements for the trapezoidal estimate.
Measurements are assumed to be accurate for this demonstration.
The dataset is illustrative and does not represent actual household meter records.
3. Input Data

Time in hours:

[0, 2, 4, 6, 8, 10, 12]

Power in kilowatts:

[0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9]

4. Mathematical Method

Estimate energy using numerical integration:

Energy = integral of power with respect to time.

The trapezoidal rule approximates the area under the power-versus-time curve.

5. Implementation

Use NumPy to store the measurements and SciPy to calculate the integral. Save the program as:

code/Task_16_numerical_integration.py

6. Parameter Experiment

Increase all power readings by 10%. Run the calculation again and compare the estimated energy with the original result.

7. Output and Interpretation

Record the actual numerical estimates produced by the program.

If every power measurement increases by 10%, the trapezoidal energy estimate also increases by 10%. The result represents estimated energy consumption in kilowatt-hours (kWh).

8. Limitations

The estimate depends on the measurement frequency and the assumption about power between readings. More frequent measurements may capture short-lived changes in electricity demand more accurately.

9. Conclusion

Numerical integration can estimate accumulated electricity consumption from discrete smart-meter readings. The method is useful for energy monitoring, household budgeting, and comparing consumption patterns.