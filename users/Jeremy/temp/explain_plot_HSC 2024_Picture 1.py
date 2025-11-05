import matplotlib.pyplot as plt
import numpy as np

def generate_plot():
    # Define the polynomial function
    def P(x):
        return x**3 + 2*x**2 - 5*x - 6

    # Generate x values for the plot
    x_vals = np.linspace(-4.5, 3.5, 400)
    # Calculate corresponding y values
    y_vals = P(x_vals)

    # The roots found from the problem are -1, -3, and 2
    roots = [-1, -3, 2]

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 7))

    # Plot the polynomial curve
    ax.plot(x_vals, y_vals, label=r'$P(x) = x^3 + 2x^2 - 5x - 6$', color='blue', linewidth=2)

    # Plot the zeros (roots) as red dots
    ax.scatter(roots, [0, 0, 0], color='red', s=150, zorder=5, label='Zeros', edgecolors='black')

    # Annotate the zeros
    for r in roots:
        ax.annotate(f'({r}, 0)', (r, 0), textcoords="offset points", xytext=(0,15),
                    ha='center', color='red', fontsize=12, fontweight='bold')

    # Add labels and title
    ax.set_xlabel('x', fontsize=14)
    ax.set_ylabel('P(x)', fontsize=14)
    ax.set_title('Graph of the Polynomial and its Zeros', fontsize=16, pad=20)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.legend(fontsize=12)

    # Set plot limits for better visualization
    ax.set_xlim([-4.5, 3.5])
    ax.set_ylim([-15, 10])

    plt.tight_layout()
    return fig