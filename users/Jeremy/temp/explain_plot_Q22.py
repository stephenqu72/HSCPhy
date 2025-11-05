import matplotlib.pyplot as plt
import numpy as np

def generate_plot():
    fig, ax = plt.subplots(figsize=(6, 3))

    # Electric field lines pointing right
    for i in range(-1, 2):
        ax.arrow(-1, i * 0.5, 3, 0, head_width=0.2, head_length=0.2, fc='blue', ec='blue')
    ax.text(2.5, -0.7, 'E', fontsize=14, color='blue')

    # Electron position
    electron_x = 0.5
    electron_y = 0
    ax.plot(electron_x, electron_y, 'o', color='red', markersize=10)
    ax.text(electron_x - 0.1, electron_y - 0.1, '−', color='white', fontsize=12, ha='center', va='center')

    # Force on electron (pointing left)
    ax.arrow(electron_x + 0.5, electron_y, -0.8, 0, head_width=0.2, head_length=0.2, fc='green', ec='green', linewidth=2)
    ax.text(electron_x + 0.8, electron_y + 0.3, 'F', fontsize=14, color='green')

    ax.set_xlim(-2, 3.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.set_title('Electron in a Uniform Electric Field')
    ax.axis('off')

    return fig
