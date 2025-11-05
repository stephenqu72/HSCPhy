import matplotlib.pyplot as plt
import numpy as np

def generate_plot():
    time_points = [0, 4, 6, 8, 9, 10]
    velocity_points = [-8, 0, 0, 5, 5, 0]

    # Create piecewise functions for velocity for shading
    t_segment1 = np.linspace(0, 4, 100)
    v_segment1 = -8 + (8/4) * t_segment1

    t_segment2 = np.linspace(4, 6, 100)
    v_segment2 = np.zeros_like(t_segment2)

    t_segment3 = np.linspace(6, 8, 100)
    v_segment3 = (5/2) * (t_segment3 - 6)

    t_segment4 = np.linspace(8, 9, 100)
    v_segment4 = np.full_like(t_segment4, 5)

    t_segment5 = np.linspace(9, 10, 100)
    v_segment5 = 5 - (5/1) * (t_segment5 - 9)

    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the main velocity-time graph
    ax.plot(time_points, velocity_points, color='black', linewidth=2)

    # Shade areas
    ax.fill_between(t_segment1, v_segment1, 0, where=(v_segment1 < 0), color='salmon', alpha=0.6, label='Negative Displacement (West)')
    ax.fill_between(t_segment3, v_segment3, 0, where=(v_segment3 > 0), color='lightgreen', alpha=0.6, label='Positive Displacement (East)')
    ax.fill_between(t_segment4, v_segment4, 0, where=(v_segment4 > 0), color='lightgreen', alpha=0.6)
    ax.fill_between(t_segment5, v_segment5, 0, where=(v_segment5 > 0), color='lightgreen', alpha=0.6)

    # Add grid lines
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_xticks(np.arange(0, 11, 1))
    ax.set_yticks(np.arange(-8, 11, 1))
    ax.set_ylim(-10, 10) # Adjust y-limits for better visualization

    # Axis labels and title
    ax.set_xlabel('Time (s)', fontsize=12)
    ax.set_ylabel('Velocity (m s$^{-1}$ east)', fontsize=12)
    ax.set_title('Velocity-Time Graph for Displacement Calculation', fontsize=14)
    ax.axhline(0, color='black', linewidth=0.5) # x-axis line
    ax.axvline(0, color='black', linewidth=0.5) # y-axis line

    # Add markers for the given points
    ax.plot(time_points, velocity_points, 'o', color='black', markersize=5)

    # Add annotations for calculated areas
    ax.text(2, -4, r'$A_1 = -16 	ext{ m}$', horizontalalignment='center', color='darkred', fontsize=10, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(7, 2.5, r'$A_3 = +5 	ext{ m}$', horizontalalignment='center', color='darkgreen', fontsize=10, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(8.5, 2.5, r'$A_4 = +5 	ext{ m}$', horizontalalignment='center', color='darkgreen', fontsize=10, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(9.5, 2.5, r'$A_5 = +2.5 	ext{ m}$', horizontalalignment='center', color='darkgreen', fontsize=10, bbox=dict(facecolor='white', alpha=0.7))
    ax.text(5, 0.5, r'$A_2 = 0 	ext{ m}$', horizontalalignment='center', color='gray', fontsize=10, bbox=dict(facecolor='white', alpha=0.7))


    ax.legend()
    plt.tight_layout()
    return fig