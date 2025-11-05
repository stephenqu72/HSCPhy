import matplotlib.pyplot as plt
import numpy as np

def generate_plot():
    x = np.linspace(0, 4, 500)
    # Handle potential non-positive values due to floating point precision, though domain ensures it
    y = np.sqrt(np.maximum(0, 2 - np.sqrt(x)))

    fig, ax = plt.subplots(figsize=(10, 7))

    # Plot the function curve
    ax.plot(x, y, label=r'$f(x) = \sqrt{2 - \sqrt{x}}$', color='#1f77b4', linewidth=2) # blue

    # Shade the area under the curve
    ax.fill_between(x, y, color='#aec7e8', alpha=0.6, label='Area bounded by the curve, x and y axes') # light blue

    # Mark key points
    y_intercept = np.sqrt(2)
    x_intercept = 4
    ax.plot(0, y_intercept, 'ro', markersize=6, label=r'y-intercept $(0, \sqrt{2})$') # red dot for y-intercept
    ax.plot(x_intercept, 0, 'go', markersize=6, label=r'x-intercept $(4, 0)$') # green dot for x-intercept

    # Annotate intercepts
    ax.text(0.1, y_intercept + 0.1, r'$(0, \sqrt{2})$', verticalalignment='bottom', horizontalalignment='left', fontsize=10)
    ax.text(x_intercept - 0.1, 0.1, r'$(4, 0)$', verticalalignment='bottom', horizontalalignment='right', fontsize=10)

    # Add axis labels and title
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('f(x)', fontsize=12)
    ax.set_title(r'Graph of $f(x) = \sqrt{2 - \sqrt{x}}$ and Bounded Area', fontsize=14)

    # Set grid and legend
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend(fontsize=10, loc='upper right')

    # Set axis limits for better viewing
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.2, np.sqrt(2) + 0.5)

    # Add a text annotation for decreasing function
    ax.text(2, 1.3, 'Decreasing Function', ha='center', va='center', fontsize=12, color='darkgreen',
            bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.5'))
            
    return fig