import matplotlib.pyplot as plt
import numpy as np

def generate_plot():
    # Data from the graph in the question
    # The line passes through (0,0) and (8mm, 22N), (10mm, 27.5N), (16mm, 44N).
    # The slope is T / Extension = 22 N / 8 mm = 2.75 N/mm.
    slope = 2.75 # N/mm

    extension_mm = np.linspace(0, 16, 100) # Extension from 0 to 16 mm
    tension_N = slope * extension_mm

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(extension_mm, tension_N, color='red', linewidth=2, label='Tension vs. Extension')

    # Set grid to match the original image (major and minor ticks)
    ax.set_xticks(np.arange(0, 17, 2))
    ax.set_yticks(np.arange(0, 41, 5))
    ax.set_xticks(np.arange(0, 17, 0.4), minor=True) # Minor ticks for every 0.4mm
    ax.set_yticks(np.arange(0, 41, 0.5), minor=True) # Minor ticks for every 0.5N
    ax.grid(which='both', linestyle='-', linewidth=0.5, color='gray', alpha=0.7)
    ax.grid(which='major', linestyle='-', linewidth=0.7, color='black', alpha=0.9)


    # Set labels and title
    ax.set_xlabel('Extension of String [mm]', fontsize=12)
    ax.set_ylabel('T [N]', fontsize=12)
    ax.set_title('Tension in String vs. Extension of String', fontsize=14)

    # Set limits to match the original graph's visible area
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 40)

    ax.legend()
    plt.tight_layout()
    return fig