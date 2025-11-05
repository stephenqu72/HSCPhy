import matplotlib.pyplot as plt
import numpy as np

def generate_plot():
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    fig.suptitle('Position of 1.00 m Emitter for Part (a)', fontsize=14)

    radius_emitter = 1.00
    # Center of circle (student's hand)
    center = (0, 0)

    # Microphone position is assumed to be far to the right.

    # --- Diagram for 0.560 m Wavelength (no Doppler shift) ---
    ax1 = axes[0]
    ax1.set_title('i. λ = 0.560 m (No Doppler Shift)')
    ax1.set_aspect('equal', adjustable='box')
    ax1.set_xlim(-1.2, 1.2)
    ax1.set_ylim(-1.2, 1.2)
    ax1.set_xticks([])
    ax1.set_yticks([])

    # Draw circular path
    theta = np.linspace(0, 2*np.pi, 100)
    ax1.plot(center[0] + radius_emitter * np.cos(theta), center[1] + radius_emitter * np.sin(theta), 'k--', linewidth=0.8)

    # Emitter position (at the top, velocity perpendicular to line of sight to the right)
    # Velocity direction: tangential to circle, perpendicular to line of sight to microphone (assumed right).
    # So, at top or bottom. Let's pick top (0, 1).
    emitter_x_1 = 0
    emitter_y_1 = radius_emitter
    ax1.plot(emitter_x_1, emitter_y_1, 'ro', markersize=10, label='Emitter')

    # Velocity vector (horizontal, tangential)
    ax1.arrow(emitter_x_1, emitter_y_1, 0.2, 0, head_width=0.08, head_length=0.08, fc='b', ec='b')
    ax1.text(emitter_x_1 + 0.25, emitter_y_1 - 0.05, r'v', color='b', ha='left', va='center', fontsize=12)

    # Label for radius
    ax1.plot([center[0], emitter_x_1], [center[1], emitter_y_1], 'k:', linewidth=0.7)
    ax1.text(0.1, 0.5, '1.00 m', rotation=90, ha='left', va='center', fontsize=9)
    ax1.text(0.5, -1.2, 'Microphone assumed to be on the right', ha='center', va='top', fontsize=8, color='gray')


    # --- Diagram for Smallest Wavelength ---
    ax2 = axes[1]
    ax2.set_title('ii. Smallest Wavelength Produced')
    ax2.set_aspect('equal', adjustable='box')
    ax2.set_xlim(-1.2, 1.2)
    ax2.set_ylim(-1.2, 1.2)
    ax2.set_xticks([])
    ax2.set_yticks([])

    # Draw circular path
    ax2.plot(center[0] + radius_emitter * np.cos(theta), center[1] + radius_emitter * np.sin(theta), 'k--', linewidth=0.8)

    # Emitter position (at the left, moving directly towards the microphone on the right)
    emitter_x_2 = -radius_emitter
    emitter_y_2 = 0
    ax2.plot(emitter_x_2, emitter_y_2, 'ro', markersize=10)

    # Velocity vector (horizontal, pointing right, towards microphone)
    ax2.arrow(emitter_x_2, emitter_y_2, 0.2, 0, head_width=0.08, head_length=0.08, fc='b', ec='b')
    ax2.text(emitter_x_2 + 0.25, emitter_y_2 - 0.05, r'v', color='b', ha='left', va='center', fontsize=12)

    # Label for radius
    ax2.plot([center[0], emitter_x_2], [center[1], emitter_y_2], 'k:', linewidth=0.7)
    ax2.text(-0.5, 0.1, '1.00 m', ha='center', va='bottom', fontsize=9)
    ax2.text(0.5, -1.2, 'Microphone assumed to be on the right', ha='center', va='top', fontsize=8, color='gray')


    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    return fig