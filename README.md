# 2D Kinematic Target Tracking & PID Gain Optimization

A numerical simulation evaluating discrete-time PID controllers tracking stochastic target trajectories in 2D space. The simulator models physical actuator saturation limits and optimizes gains via multi-decade logarithmic search using an Integrated Squared Tracking Error (IST) objective function.

---

## Visuals & Performance

| Trajectory Tracking | Error Convergence |
| :---: | :---: |
| ![Tracking Demo](docs/tracking_animation.gif) | ![Error vs Time](docs/error_response.png) |
| *Chaser trajectory converging to stochastic target* | *Step-response settling and steady-state tracking* |

---

## Key Features

* **Physics & Kinematics Modeling:** Discrete-time numerical integration ($\Delta t = 10^{-3}\text{ s}$) with non-linear actuator acceleration limits ($a_{\text{max}}$ saturation).
* **Robust Derivative Handling:** Implements derivative-on-measurement damping to prevent high-frequency acceleration spikes (derivative kick) during abrupt setpoint shifts.
* **Logarithmic Grid Search Optimization:** Automated exploration across $K_p \in [10^{-1}, 10^5]$, $K_i \in [10^{-4}, 10^1]$, and $K_d \in [10^{-2}, 10^3]$ parameter spaces.
* **Performance Metric Evaluation:** Evaluates control quality via Integrated Squared Tracking Error (IST) while discarding initial slew saturation:
  $$\text{IST} = \int_{t_{\text{settle}}}^{t_{\text{end}}} \Vert{}\mathbf{e}(t)\Vert{}^2 \, dt$$

---

## Control Law & Dynamics

The acceleration control command $\mathbf{u}(t)$ for the 2D chaser agent is computed as:

$$\mathbf{e}(t) = \mathbf{x}_{\text{target}}(t) - \mathbf{x}_{\text{chaser}}(t)$$

$$\mathbf{u}(t) = K_p \mathbf{e}(t) + K_i \int_0^t \mathbf{e}(\tau) d\tau - K_d \mathbf{v}_{\text{chaser}}(t)$$

$$\mathbf{a}_{\text{chaser}}(t) = \text{clip}\left(\mathbf{u}(t), -a_{\text{max}}, a_{\text{max}}\right)$$

$$\mathbf{v}_{\text{chaser}}(t + \Delta t) = \mathbf{v}_{\text{chaser}}(t) + \mathbf{a}_{\text{chaser}}(t)\Delta t$$

$$\mathbf{x}_{\text{chaser}}(t + \Delta t) = \mathbf{x}_{\text{chaser}}(t) + \mathbf{v}_{\text{chaser}}(t)\Delta t$$

---

## Optimization Results

| Rank | $K_p$ | $K_i$ | $K_d$ | IST Score | Steady-State Error |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Best (#1)** | 1668.10 | 0.0046 | 464.16 | **9382.26** | **0.029** |
| **Top 2** | 599.48 | 0.7743 | 215.44 | 9945.52 | 0.265 |
| **Top 3** | 1668.10 | 0.0004 | 464.16 | 10184.60 | 0.033 |
| **Worst** | 10.00 | 0.0013 | 1000.00 | 275912.45 | 1.012 |

---

## Getting Started

### Prerequisites
* Python 3.8+
* `numpy`
* `matplotlib`

```bash
pip install numpy matplotlib

git clone [https://github.com/WyattBuller-projects/2D_PID.git](https://github.com/WyattBuller-projects/2D_PID.git)
cd 2D_PID
python pid_simulation.py

├── docs/
│   ├── tracking_animation.gif   # Visual trajectory render
│   └── error_response.png       # Settling time & error plots
├── pid_simulation.py            # Simulation engine & grid search optimizer
└── README.md                    # Project documentation