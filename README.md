# 2D PID Control and Gain Search

A numerical simulation of a discrete-time PID controller tracking a randomly moving target in two-dimensional space. The simulation models a chaser attempting to follow a target whose velocity changes randomly over time, evaluating 1,000 combinations of PID gains and ranking their performance using Integrated Squared Tracking Error (IST).

-

## Overview

The simulation includes:
* 2D target and chaser motion
* Discrete-time PID control
* Position, velocity, and acceleration states
* Component-wise acceleration limits
* Numerical integration with a fixed timestep
* Automated PID gain search across logarithmic scales
* Integrated Squared Tracking Error (IST) evaluation
* Comparative performance ranking of the five lowest-IST controllers

---

## Simulation Setup

The simulation runs for $4\text{ s}$ with a fixed timestep:

$$\Delta t = 0.001\text{ s}$$

* **Chaser initial state:** $\mathbf{x}_{\text{chaser}}(0) = (0, 0)$, $\mathbf{v}_{\text{chaser}}(0) = (0, 0)$
* **Target initial state:** $\mathbf{x}_{\text{target}}(0) = (200, 200)$, $\mathbf{v}_{\text{target}}(0) = (0, 0)$

### Target Motion
At each timestep, the target velocity changes along one of four cardinal directions ($+x, -x, +y, -y$). The velocity step size is:

$$\Delta v = 1000 \Delta t = 1.0$$

---

## Control Law & Dynamics

### Error Formulation
$$\mathbf{e}(t) = \mathbf{x}_{\text{target}}(t) - \mathbf{x}_{\text{chaser}}(t)$$

### Commanded Acceleration
$$\mathbf{a}_{\text{cmd}}(t) = K_p \mathbf{e}(t) + K_i \int_0^t \mathbf{e}(\tau) \, d\tau + K_d \frac{d\mathbf{e}(t)}{dt}$$

The derivative term is approximated backward in discrete time:

$$\frac{d\mathbf{e}(t)}{dt} \approx \frac{\mathbf{e}_n - \mathbf{e}_{n-1}}{\Delta t}$$

### Actuator Saturation & Anti-Windup
Commanded acceleration is clipped component-wise:

$$-500 \le a_x, a_y \le 500$$

The integral error accumulates only when the previously applied acceleration magnitude is below the saturation threshold.

### Numerical Integration (Semi-Implicit Euler)
$$\mathbf{v}_{n+1} = \mathbf{v}_n + \mathbf{a}_n \Delta t$$

$$\mathbf{x}_{n+1} = \mathbf{x}_n + \mathbf{v}_{n+1} \Delta t$$

$$\mathbf{x}_{\text{target}, n+1} = \mathbf{x}_{\text{target}, n} + \mathbf{v}_{\text{target}, n} \Delta t$$

---

## PID Gain Search

The optimization evaluates a $10 \times 10 \times 10$ parameter space ($1{,}000$ total configurations):

* **Proportional ($K_p$):** 10 values from $\operatorname{logspace}(1, 5, 10)$
* **Integral ($K_i$):** 9 values from $\operatorname{logspace}(-4, 1, 10)$ plus $K_i = 0$
* **Derivative ($K_d$):** 10 values from $\operatorname{logspace}(0, 2, 10)$

---

## Performance Metric

Controllers are ranked using Integrated Squared Tracking Error (IST). The initial transient phase ($t < 0.4\text{ s}$, first 10%) is excluded to evaluate steady-state tracking performance:

$$\text{IST} = \int_{0.4}^{4.0} \Vert{}\mathbf{e}(t)\Vert{}^2 \, dt \approx \sum_{n=400}^{3999} \Vert{}\mathbf{e}_n\Vert{}^2 \Delta t$$

---

## Results & Analysis

After evaluating all 1,000 gain combinations, the script:
1. Calculates the IST metric for every gain set.
2. Identifies and prints the top 5 lowest-IST controllers and the highest-IST controller.
3. Reports final error magnitudes for top performers.
4. Generates comparative tracking error response curves.

---

## Getting Started

### Prerequisites
* Python 3.8+
* NumPy
* Matplotlib

```bash
pip install numpy matplotlib

Then run:

```bash
python 2D_PID.py