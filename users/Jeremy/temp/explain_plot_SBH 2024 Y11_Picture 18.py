import matplotlib.pyplot as plt
import numpy as np

def generate_plot():
    fig, ax = plt.subplots(figsize=(8, 2))

    # Charge positions (symbolic relative positions)
    electron_pos = 0
    q1_pos = 1  # Represents d
    q2_pos = 2  # Represents 2d

    # Draw charges
    ax.plot(electron_pos, 0, 'o', color='blue', markersize=10)
    ax.text(electron_pos, 0.2, 'Electron ($q_e$)', ha='center', va='bottom', fontsize=10)

    ax.plot(q1_pos, 0, 'o', color='red', markersize=10)
    ax.text(q1_pos, 0.2, '$+1.0 \, \mu C$ ($Q_1$)', ha='center', va='bottom', fontsize=10)

    ax.plot(q2_pos, 0, 'o', color='green', markersize=10)
    ax.text(q2_pos, 0.2, '$q$ ($Q_2$)', ha='center', va='bottom', fontsize=10)

    # Distances
    ax.plot([electron_pos, q1_pos], [0.05, 0.05], 'k--')
    ax.text((electron_pos + q1_pos) / 2, 0.1, '$d$', ha='center', va='bottom', fontsize=10)

    ax.plot([q1_pos, q2_pos], [0.05, 0.05], 'k--')
    ax.text((q1_pos + q2_pos) / 2, 0.1, '$d$', ha='center', va='bottom', fontsize=10)

    # Forces on the electron
    # F_1: Attraction towards +1.0 \mu C (positive x direction)
    ax.arrow(electron_pos, -0.5, 0.5, 0, head_width=0.08, head_length=0.1, fc='purple', ec='purple', lw=1.5, zorder=5)
    ax.text(electron_pos + 0.25, -0.6, '$F_1$', ha='center', va='top', fontsize=10, color='purple')

    # F_2: Repulsion from q (negative x direction, for net force to be zero)
    ax.arrow(electron_pos, -0.5, -0.5, 0, head_width=0.08, head_length=0.1, fc='orange', ec='orange', lw=1.5, zorder=5)
    ax.text(electron_pos - 0.25, -0.6, '$F_2$', ha='center', va='top', fontsize=10, color='orange')


    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-1, 1)
    ax.axis('off') # Hide axes

    ax.set_title('Forces on the Electron for Net Force = 0', fontsize=12)
    plt.tight_layout()
    return fig