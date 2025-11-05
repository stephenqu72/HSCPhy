import matplotlib.pyplot as plt
import io
import base64

def generate_plot():
    fig, ax = plt.subplots(figsize=(6, 4))

    # Trough: Apex at (0,0), top base extending from (-75, 25) to (75, 25)
    # Total width = 150 cm (1.5 m), Total height = 25 cm.
    trough_x = [-75, 75, 0, -75]
    trough_y = [25, 25, 0, 25]
    ax.plot(trough_x, trough_y, 'b-', linewidth=2, label='Trough End')

    # Water: At depth h, width x
    # For illustration, let's pick h = 20 cm, as used in part (ii)
    h_illustrative = 20
    # From similar triangles: x/h = 150/25 => x = 6h
    x_illustrative = 6 * h_illustrative # 120 cm
    
    water_x_coords = [-x_illustrative/2, x_illustrative/2]
    water_y_coords = [h_illustrative, h_illustrative]
    ax.plot(water_x_coords, water_y_coords, 'c--', linewidth=1.5, label=f'Water Surface (h={h_illustrative}cm)')
    
    # Fill the water area for better visualization
    ax.fill_between([0, x_illustrative/2], [0, h_illustrative], color='lightblue', alpha=0.5)
    ax.fill_between([-x_illustrative/2, 0], [h_illustrative, 0], color='lightblue', alpha=0.5)

    # Annotations for trough dimensions
    ax.plot([75, 75], [0, 25], 'k:', alpha=0.7) # Dotted line for height
    ax.plot([-75, 75], [25, 25], 'k:', alpha=0.7) # Dotted line for width
    ax.text(0, 26, '150 cm (1.5 m)', ha='center', va='bottom', fontsize=9)
    ax.text(-80, 12.5, '25 cm', ha='right', va='center', rotation=90, fontsize=9)

    # Annotations for water dimensions
    ax.plot([x_illustrative/2, x_illustrative/2], [0, h_illustrative], 'k:', alpha=0.7)
    ax.plot([-x_illustrative/2, x_illustrative/2], [h_illustrative, h_illustrative], 'k:', alpha=0.7)
    ax.text(0, h_illustrative + 1, f'x cm', ha='center', va='bottom', fontsize=9, color='darkcyan')
    ax.text(-x_illustrative/2 - 5, h_illustrative/2, f'h cm', ha='right', va='center', rotation=90, fontsize=9, color='darkcyan')


    ax.set_aspect('equal', adjustable='box')
    ax.set_title('Triangular Cross-section of Water Trough (Similar Triangles)')
    ax.set_xlabel('Width (cm)')
    ax.set_ylabel('Height (cm)')
    ax.set_xlim(-90, 90)
    ax.set_ylim(-5, 30)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend(loc='upper right', fontsize=8)

    return fig