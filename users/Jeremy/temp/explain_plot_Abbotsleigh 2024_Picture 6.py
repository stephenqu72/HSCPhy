import matplotlib.pyplot as plt
import numpy as np

def generate_plot():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, linestyle='--', alpha=0.6)

    # Define vectors u and v based on the diagram's general direction
    u = np.array([2, 3])
    v = np.array([3, -2]) # v points down and right

    # Origin
    origin = np.array([0, 0])

    # Plot vector u
    ax.quiver(*origin, *u, angles='xy', scale_units='xy', scale=1, color='black', label='u', width=0.005)
    ax.text(u[0] * 0.5 - 0.1, u[1] * 0.5 + 0.3, r'$\mathbf{u}$', color='black', ha='center', va='bottom', fontsize=14)

    # Plot vector v (from origin, for reference)
    ax.quiver(*origin, *v, angles='xy', scale_units='xy', scale=1, color='black', width=0.005)
    ax.text(v[0] * 0.5 + 0.3, v[1] * 0.5 - 0.3, r'$\mathbf{v}$', color='black', ha='left', va='top', fontsize=14)

    # --- Construction for r1 = u + v ---
    r1 = u + v
    # Plot v_1 (parallel to v, equal length to v) from head of u
    ax.quiver(*u, *v, angles='xy', scale_units='xy', scale=1, color='gray', linestyle='--', linewidth=1, alpha=0.7, width=0.003)
    ax.text(u[0] + v[0] * 0.5 + 0.2, u[1] + v[1] * 0.5 - 0.2, r'$\mathbf{v_1}$', color='gray', ha='left', va='top', fontsize=12)
    # Plot r1
    ax.quiver(*origin, *r1, angles='xy', scale_units='xy', scale=1, color='black', width=0.005)
    ax.text(r1[0] * 0.5 - 0.2, r1[1] * 0.5 - 0.2, r'$\mathbf{r_1}$', color='black', ha='right', va='top', fontsize=14)

    # --- Construction for r2 = u - v ---
    # We know r2 + v_2 = u, where v_2 = v. So r2 = u - v.
    r2 = u - v
    # Plot r2
    ax.quiver(*origin, *r2, angles='xy', scale_units='xy', scale=1, color='black', width=0.005)
    ax.text(r2[0] * 0.5 - 0.2, r2[1] * 0.5 + 0.2, r'$\mathbf{r_2}$', color='black', ha='right', va='bottom', fontsize=14)
    # Plot v_2 (parallel to v, equal length to v) from head of r2 to head of u
    # The vector from head of r2 to head of u is u - r2. If this is v, then r2 = u - v.
    ax.quiver(*r2, *(u - r2), angles='xy', scale_units='xy', scale=1, color='gray', linestyle='--', linewidth=1, alpha=0.7, width=0.003)
    ax.text(r2[0] + (u[0]-r2[0]) * 0.5 + 0.2, r2[1] + (u[1]-r2[1]) * 0.5 - 0.2, r'$\mathbf{v_2}$', color='gray', ha='left', va='top', fontsize=12)


    ax.set_xlim(-2, 6)
    ax.set_ylim(-3, 6)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Vector Addition and Subtraction')
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    
    return fig