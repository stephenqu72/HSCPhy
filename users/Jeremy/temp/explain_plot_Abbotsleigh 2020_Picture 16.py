import matplotlib.pyplot as plt
import numpy as np
import io
import base64

def generate_plot():
    fig, ax = plt.subplots(figsize=(6, 5))

    # Define coordinates for a right-angled triangle where B is the origin.
    # This is an example to visualize the vectors and the theorem.
    points = {
        'A': np.array([0, 3]),
        'B': np.array([0, 0]),
        'C': np.array([4, 0]),
        'M': np.array([2, 1.5]) # Midpoint of AC
    }

    # Plot the triangle ABC
    ax.plot([points['A'][0], points['B'][0], points['C'][0], points['A'][0]],
            [points['A'][1], points['B'][1], points['C'][1], points['A'][1]], 'k-')
    ax.text(points['A'][0] - 0.1, points['A'][1] + 0.1, 'A', ha='right', va='bottom')
    ax.text(points['B'][0] - 0.2, points['B'][1] - 0.2, 'B', ha='right', va='top')
    ax.text(points['C'][0] + 0.1, points['C'][1] - 0.1, 'C', ha='left', va='top')
    ax.text(points['M'][0], points['M'][1] + 0.1, 'M', ha='center', va='bottom')

    # Indicate right angle at B with a square symbol
    ax.plot([0, 0.3, 0.3], [0.3, 0.3, 0], 'k-', linewidth=0.8)

    # Draw and label given vectors AM (vector a) and BM (vector b)
    vec_AM = points['M'] - points['A']
    vec_BM = points['M'] - points['B']

    # Vector AM (a)
    ax.arrow(points['A'][0], points['A'][1], vec_AM[0], vec_AM[1],
             head_width=0.1, head_length=0.15, fc='blue', ec='blue', length_includes_head=True, zorder=2)
    ax.text(points['A'][0] + vec_AM[0]/2 - 0.1, points['A'][1] + vec_AM[1]/2 - 0.2, '$\vec{a}$', color='blue', ha='left')

    # Vector BM (b)
    ax.arrow(points['B'][0], points['B'][1], vec_BM[0], vec_BM[1],
             head_width=0.1, head_length=0.15, fc='red', ec='red', length_includes_head=True, zorder=2)
    ax.text(points['B'][0] + vec_BM[0]/2 - 0.2, points['B'][1] + vec_BM[1]/2 + 0.1, '$\vec{b}$', color='red', ha='right')

    # Optionally, draw the vectors AB and BC for visual verification of calculations
    # These are calculated as per part (i):
    # vec_AB = vec_BM - vec_AM  (i.e., b - a)
    # vec_BC = vec_BM + vec_AM  (i.e., b + a)
    
    # Vector AB (b - a)
    vec_AB_calc = points['B'] - points['A'] # From the coordinates
    # Or, as calculated: vec_BM - vec_AM = np.array([2, 1.5]) - np.array([2, -1.5]) = np.array([0, 3])
    ax.arrow(points['B'][0], points['B'][1], vec_AB_calc[0], vec_AB_calc[1],
             head_width=0.1, head_length=0.15, fc='green', ec='green', ls='--', length_includes_head=True, zorder=1)
    ax.text(points['B'][0] + vec_AB_calc[0]/2 - 0.1, points['B'][1] + vec_AB_calc[1]/2, '$\vec{AB}$', color='green')

    # Vector BC (b + a)
    vec_BC_calc = points['C'] - points['B'] # From the coordinates
    # Or, as calculated: vec_BM + vec_AM = np.array([2, 1.5]) + np.array([2, -1.5]) = np.array([4, 0])
    ax.arrow(points['B'][0], points['B'][1], vec_BC_calc[0], vec_BC_calc[1],
             head_width=0.1, head_length=0.15, fc='purple', ec='purple', ls='--', length_includes_head=True, zorder=1)
    ax.text(points['B'][0] + vec_BC_calc[0]/2 + 0.1, points['B'][1] + vec_BC_calc[1]/2, '$\vec{BC}$', color='purple')

    # Draw lines from M to A, B, C to show equidistance visually
    ax.plot([points['M'][0], points['A'][0]], [points['M'][1], points['A'][1]], 'b:')
    ax.plot([points['M'][0], points['B'][0]], [points['M'][1], points['B'][1]], 'r:')
    ax.plot([points['M'][0], points['C'][0]], [points['M'][1], points['C'][1]], 'g:')
    

    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, linestyle=':', alpha=0.7)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Vector Diagram: Right-Angled Triangle ABC')
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.5, 3.5)
    
    return fig