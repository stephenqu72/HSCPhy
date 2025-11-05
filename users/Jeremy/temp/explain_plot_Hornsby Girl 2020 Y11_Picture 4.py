import matplotlib.pyplot as plt
import numpy as np

def generate_plot():
    fig, ax = plt.subplots(figsize=(8, 6))

    # PPF curve points - estimated to match the visual representation
    # Using a cubic function for a bowed-out shape for illustration
    x_ppf = np.linspace(0, 10, 100)
    y_ppf = 10 * np.power(1 - (x_ppf/10)**3, 1/3) # A general equation for bowed-out PPF

    # Plot the PPF curve
    ax.plot(x_ppf, y_ppf, color='blue', linewidth=2)

    # Points A, B, C as estimated from the image
    points = {
        'A': (8.5, 3.0),
        'B': (5.5, 6.5),
        'C': (2.5, 9.0)
    }

    # Plot points A, B, C and add dashed lines to axes
    for label, (x, y) in points.items():
        ax.plot(x, y, 'o', color='red')
        ax.text(x + 0.3, y, label, fontsize=12, ha='left', va='center')
        ax.plot([x, x], [0, y], 'k--', linewidth=0.8, dashes=(5, 5))
        ax.plot([0, x], [y, y], 'k--', linewidth=0.8, dashes=(5, 5))

    # Set labels and title
    ax.set_xlabel('Capital goods', fontsize=12)
    ax.set_ylabel('Consumer goods', fontsize=12)
    ax.set_title('Production Possibility Frontier (PPF)', fontsize=14)

    # Set limits and ticks
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 10.5)
    ax.set_xticks(np.arange(0, 11, 2))
    ax.set_yticks(np.arange(0, 11, 2))

    # Remove top and right spines for a cleaner look consistent with the original diagram
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # Add origin label
    ax.text(0.1, -0.5, '0', fontsize=12, ha='center', va='top')

    plt.tight_layout()
    return fig