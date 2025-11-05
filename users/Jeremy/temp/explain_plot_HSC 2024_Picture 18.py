import matplotlib.pyplot as plt
import numpy as np
import base64
from io import BytesIO

def generate_plot():
    # Define the polynomial function f(a) = a^3 + 5a^2 + 2a - 8
    # This function's roots are the solutions to the problem.
    def f_a_func(a):
        return a**3 + 5*a**2 + 2*a - 8

    # Generate a range of 'a' values to plot the function
    a_values = np.linspace(-5, 2, 400) # Range chosen to clearly show all three roots
    f_a = f_a_func(a_values)

    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the function
    ax.plot(a_values, f_a, label=r'$f(a) = a^3 + 5a^2 + 2a - 8$', color='blue', linewidth=2)

    # Mark the roots found (where f(a) = 0)
    roots = [-4, -2, 1]
    for root in roots:
        ax.plot(root, 0, 'ro', markersize=8, zorder=5) # 'ro' for red circle
        ax.axvline(x=root, color='grey', linestyle='--', linewidth=0.7, zorder=0) # Vertical dashed lines at roots
        ax.text(root, 0.5, f'$a={root}$', ha='center', va='bottom', fontsize=10, color='red')

    # Add horizontal and vertical axes for clarity
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)

    # Set title and labels
    ax.set_title('Graph of $f(a) = a^3 + 5a^2 + 2a - 8$ (Identifying Roots)', fontsize=14)
    ax.set_xlabel('$a$', fontsize=12)
    ax.set_ylabel('$f(a)$', fontsize=12)

    # Add grid for better readability
    ax.grid(True, linestyle='--', alpha=0.6)

    # Add a legend
    ax.legend(fontsize=11)

    # Adjust y-axis limits to ensure roots and curve behavior around them are clearly visible
    ax.set_ylim(-15, 15) 

    # Use tight_layout to ensure all elements fit within the figure area
    fig.tight_layout()

    return fig