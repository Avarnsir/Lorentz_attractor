import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 1. Define the system of Lorenz differential equations
def lorenz_system(t, state, sigma, rho, beta):
    x, y, z = state
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return [dx_dt, dy_dt, dz_dt]

# 2. Set up the initial conditions and time span
initial_state = [0.1, 1.0, 1.05]
t_span = (0, 40)
t_eval = np.linspace(t_span[0], t_span[1], 4000)

# 3. Create the Matplotlib layout (Plot on top, Sliders at the bottom)
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.25)  # Make room for sliders

# Initial integration parameters
init_sigma, init_rho, init_beta = 10.0, 28.0, 8.0/3.0

# Function to solve and update the trajectory data
def compute_trajectory(s, r, b):
    sol = solve_ivp(lorenz_system, t_span, initial_state, args=(s, r, b), t_eval=t_eval)
    return sol.y[0], sol.y[1], sol.y[2]

# Compute initial line segment (Fixed the color bug here)
x_data, y_data, z_data = compute_trajectory(init_sigma, init_rho, init_beta)
line, = ax.plot(x_data, y_data, z_data, lw=0.7, color='purple')

# Set visual configurations for the 3D Axes
ax.set_title("Interactive 3D Lorenz Attractor", fontsize=14)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_xlim(-25, 25)
ax.set_ylim(-35, 35)
ax.set_zlim(0, 50)

# 4. Add interactive sliders (Fixed the missing quote on rho here)
ax_sigma = plt.axes([0.15, 0.15, 0.65, 0.03])
ax_rho   = plt.axes([0.15, 0.10, 0.65, 0.03])
ax_beta  = plt.axes([0.15, 0.05, 0.65, 0.03])

slider_sigma = Slider(ax_sigma, r'$\sigma$', 0.1, 30.0, valinit=init_sigma)
slider_rho   = Slider(ax_rho,   r'$\rho$',   0.1, 50.0, valinit=init_rho)
slider_beta  = Slider(ax_beta,  r'$\beta$',  0.1, 10.0, valinit=init_beta)

# 5. Define update function triggered by slider movement
def update(val):
    s = slider_sigma.val
    r = slider_rho.val
    b = slider_beta.val
    
    # Re-integrate the ODEs using the slider parameters
    new_x, new_y, new_z = compute_trajectory(s, r, b)
    
    # Dynamically fit the line graphics object with the new coordinates
    line.set_data(new_x, new_y)
    line.set_3d_properties(new_z)
    
    # Re-draw the canvas
    fig.canvas.draw_idle()

# Connect sliders to update loop
slider_sigma.on_changed(update)
slider_rho.on_changed(update)
slider_beta.on_changed(update)

plt.show()
