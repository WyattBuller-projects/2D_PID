# 2D PID Control and Gain Search

A numerical simulation of a discrete-time PID controller tracking a randomly moving target in two-dimensional space.

The project simulates a chaser attempting to follow a target whose velocity changes randomly over time. It then evaluates 1,000 different combinations of PID gains and ranks them using Integrated Squared Tracking Error (IST).

## Overview

The simulation contains:

* A target moving in 2D space using a random walk in velocity
* A chaser controlled by a PID controller
* Position, velocity, and acceleration states
* A maximum acceleration limit on the chaser
* Numerical integration with a fixed timestep
* Automated search over PID gain combinations
* Integrated Squared Tracking Error (IST) for controller evaluation
* Identification and plotting of the five lowest-IST controllers

The main implementation is written in Python using NumPy and Matplotlib.

## Simulation

The simulation uses a timestep of:

[
\Delta t = 0.001\text{ s}
]

and runs for:

[
4000\text{ steps}
]

giving a total simulated time of 4 seconds.

The chaser begins at:

[
\mathbf{x}_{chaser} = (0,0)
]

while the target begins at:

[
\mathbf{x}_{target} = (200,200)
]

Both begin with zero velocity.

### Target Motion

At every timestep, the target's velocity is randomly modified in one of four directions:

* (+x)
* (-x)
* (+y)
* (-y)

The magnitude of the velocity change is determined by:

[
1000\Delta t = 1
]

Therefore, each timestep changes one component of the target velocity by (+1) or (-1).

This produces a randomly changing target trajectory rather than a fixed setpoint.

## PID Controller

The position error is calculated as:

[
\mathbf{e}(t)
=============

## \mathbf{x}_{target}(t)

\mathbf{x}_{chaser}(t)
]

The controller calculates acceleration using:

[
\mathbf{a}_{cmd}
================

K_p\mathbf{e}
+
K_i\int\mathbf{e},dt
+
K_d\frac{d\mathbf{e}}{dt}
]

The derivative term is calculated numerically from the change in error between consecutive timesteps:

[
\frac{d\mathbf{e}}{dt}
\approx
\frac{\mathbf{e}*n-\mathbf{e}*{n-1}}{\Delta t}
]

The resulting acceleration is limited component-by-component to:

[
-500 \leq a_x,a_y \leq 500
]

using NumPy's `clip` function.

## Numerical Integration

The chaser's velocity is updated using:

[
\mathbf{v}_{n+1}
================

\mathbf{v}_n
+
\mathbf{a}_n\Delta t
]

The chaser's position is then updated using the new velocity:

[
\mathbf{x}_{n+1}
================

\mathbf{x}*n
+
\mathbf{v}*{n+1}\Delta t
]

This corresponds to a semi-implicit Euler integration step.

The target position is updated from its current velocity:

[
\mathbf{x}_{target,n+1}
=======================

\mathbf{x}*{target,n}
+
\mathbf{v}*{target,n}\Delta t
]

## Integral Term

The accumulated position error is updated numerically:

[
\mathbf{I}_{n+1}
================

\mathbf{I}_n
+
\mathbf{e}_n\Delta t
]

The integral is only updated when the magnitude of the chaser's previous acceleration is below the maximum acceleration limit.

This prevents the integral from continuing to accumulate while the controller is already at its acceleration limit.

## PID Gain Search

The program evaluates 10 values for each gain.

### Proportional Gain

[
K_p = \operatorname{logspace}(1,5,10)
]

corresponding to values between:

[
10^1
\text{ and }
10^5
]

### Integral Gain

[
K_i = \operatorname{logspace}(-4,1,10)
]

with the final value replaced by zero.

Therefore, the simulation tests nine logarithmically spaced nonzero values between (10^{-4}) and (10^1), plus:

[
K_i=0
]

### Derivative Gain

[
K_d = \operatorname{logspace}(0,2,10)
]

corresponding to values between:

[
10^0
\text{ and }
10^2
]

The resulting search contains:

[
10\times10\times10=1000
]

different PID gain combinations.

## Performance Metric

The controller's performance is evaluated using **Integrated Squared Tracking Error (IST)**.

The magnitude of the position error is:

[
||\mathbf{e}(t)||
]

The program calculates:

[
IST
===

\int_{0.4}^{4}
||\mathbf{e}(t)||^2dt
]

numerically as:

[
IST
\approx
\sum_{n=400}^{3999}
||\mathbf{e}_n||^2\Delta t
]

The first 10% of the simulation is excluded from the calculation.

A lower IST indicates a lower accumulated squared tracking error over the evaluated portion of the simulation.

## Results

After all 1,000 simulations are completed, the program:

1. Calculates the IST for every controller.
2. Identifies the five controllers with the lowest IST.
3. Identifies the controller with the highest IST.
4. Prints the corresponding (K_p), (K_i), and (K_d) values.
5. Prints the final error magnitude for each of the five best controllers.
6. Plots the error magnitude of the five best controllers.

Because the target trajectory is generated randomly inside each individual simulation, the gain search currently evaluates each controller against its own randomly generated trajectory. The results therefore vary between program executions.

## Technologies

* **Python**
* **NumPy**
* **Matplotlib**

## Running the Simulation

Install the required packages:

```bash
pip install numpy matplotlib
```

Then run:

```bash
python 2D_PID.py
```

The program will evaluate all 1,000 gain combinations and display the error curves for the five controllers with the lowest IST.

## Project Structure

```text
2D_PID/
├── 2D_PID.py
├── 2D_PID.java
├── README.md
└── .gitattributes
```

## Future Improvements

Possible extensions to the simulation include:

* Using the same target trajectory for every PID controller to make gain comparisons directly reproducible.
* Adding baseline gains for quantitative performance comparisons.
* Evaluating additional performance metrics such as RMS error and maximum error.
* Implementing additional anti-windup methods for the integral term.
* Comparing derivative-on-error and derivative-on-measurement control.
* Improving the gain-search algorithm beyond exhaustive grid search.
* Adding real-time visualization of the target and chaser trajectories.
