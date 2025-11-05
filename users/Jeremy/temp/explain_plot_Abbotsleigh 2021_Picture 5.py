import matplotlib.pyplot as plt
import numpy as np

def generate_plot():
    fig, ax = plt.subplots(figsize=(6, 6))

    # Set up the Argand diagram axes
    ax.axhline(0, color='grey', linewidth=0.8, zorder=0)
    ax.axvline(0, color='grey', linewidth=0.8, zorder=0)
    ax.set_xlabel('$Re(z)$', fontsize=12)
    ax.set_ylabel('$Im(z)$', fontsize=12, rotation=0, ha='right')
    ax.yaxis.set_label_coords(0.5, 1.05) # Adjust position of Im(z) label
    ax.set_aspect('equal', adjustable='box')

    # Plot the origin
    ax.plot(0, 0, 'o', color='black', markersize=4, label='Origin')
    ax.text(-0.2, -0.2, 'o', ha='right', va='top')

    # Identify the starting point z_0 = 1 - i
    z0_real = 1
    z0_imag = -1

    # Plot the starting point with an open circle
    ax.plot(z0_real, z0_imag, 'o', markerfacecolor='white', markeredgecolor='black', markersize=8, label='$z_0 = 1-i$')
    
    # Define the angle
    theta = -np.pi / 4

    # Calculate points for the ray
    # The ray starts from (z0_real, z0_imag) and goes in direction theta
    length = 2 # Length of the arrow
    dx = length * np.cos(theta)
    dy = length * np.sin(theta)

    # Plot the ray as an arrow
    ax.arrow(z0_real, z0_imag, dx, dy, head_width=0.2, head_length=0.3, fc='black', ec='black', length_includes_head=True)

    # Set plot limits
    ax.set_xlim(-2, 3)
    ax.set_ylim(-3, 2)
    ax.set_xticks(np.arange(-2, 4, 1))
    ax.set_yticks(np.arange(-3, 3, 1))
    ax.grid(True, linestyle=':', alpha=0.7)

    # Add a title (optional, but good for context)
    ax.set_title(r'Argand Diagram for $\arg(z - (1-i)) = -\frac{\pi}{4}$', fontsize=14)

    return fig