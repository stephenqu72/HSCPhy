import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import io
import base64

def generate_plot():
    # Define approximate points for f(x) to capture its shape and key features
    # These points are chosen to approximate the shape of the given f(x):
    # - Approaches 0 as x -> -inf
    # - Passes through (0, 1)
    # - Has a local maximum at (1, 2)
    # - Passes through (3, 0)
    # - Becomes negative for x > 3
    x_f_points = np.array([-6, -4, -2, -1, 0, 0.5, 1, 1.5, 2, 2.5, 2.9, 3, 3.5, 4])
    y_f_points = np.array([0.05, 0.1, 0.3, 0.7, 1, 1.5, 2, 1.5, 1, 0.5, 0.1, 0, -0.5, -1])

    # Use a cubic spline to create a smooth function f(x) from these points
    f_spline = CubicSpline(x_f_points, y_f_points, bc_type='natural')

    # Generate x values for plotting
    x_vals = np.linspace(-6, 4, 500)

    # Calculate y values for f(x)
    y_f_vals = f_spline(x_vals)

    # Calculate y values for g(x) = 1 / sqrt(f(x))
    # Ensure f(x) > 0 for g(x) to be defined. Use a small positive threshold to avoid division by zero or sqrt of negative.
    y_g_vals = np.full_like(x_vals, np.nan) 
    valid_indices = y_f_vals > 1e-6 
    y_g_vals[valid_indices] = 1 / np.sqrt(y_f_vals[valid_indices])

    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot f(x) for reference
    ax.plot(x_vals, y_f_vals, label=r'$y = f(x)$', color='gray', linestyle='--')

    # Plot g(x)
    ax.plot(x_vals, y_g_vals, label=r'$y = \frac{1}{\sqrt{f(x)}}$', color='blue', linewidth=2)

    # Mark key points on f(x) and their transformations on g(x)
    # Original f(x) points
    ax.plot(0, 1, 'go', markersize=5, label=r'$(0,1)$ on $f(x)$') # (0,1)
    ax.plot(1, 2, 'ro', markersize=5, label=r'$(1,2)$ on $f(x)$ (max)') # (1,2)
    ax.plot(3, 0, 'kx', markersize=7, label=r'$(3,0)$ on $f(x)$ (x-int)') # (3,0)

    # Transformed g(x) points
    ax.plot(0, 1/np.sqrt(1), 'go', fillstyle='none', markersize=7, label=r'$(0,1)$ on $g(x)$') # (0,1)
    ax.plot(1, 1/np.sqrt(2), 'ro', fillstyle='none', markersize=7, label=r'$(1,1/\sqrt{2})$ on $g(x)$ (min)') # (1, 1/sqrt(2))
    ax.axvline(x=3, color='k', linestyle=':', label='Vertical Asymptote $x=3$') # Vertical asymptote at x=3

    # Add labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(r'Sketch of $y = \frac{1}{\sqrt{f(x)}}$ compared to $y=f(x)$')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(loc='upper left')
    ax.set_ylim([-1, 5]) # Adjust y-limits for better visualization
    ax.set_xlim([-6, 4]) # Adjust x-limits to match original graph extent

    return fig