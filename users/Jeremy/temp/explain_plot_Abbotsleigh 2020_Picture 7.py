import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def generate_plot():
    x_min, x_max = -5, 5
    y_min, y_max = -3, 5 

    # Create a grid of points
    # Adjust number of points for clarity and to match image density
    x = np.linspace(x_min, x_max, int(x_max - x_min) + 1)
    y = np.linspace(y_min, y_max, int(y_max - y_min) + 1)
    X, Y = np.meshgrid(x, y)

    # Calculate dy/dx for option C: dy/dx = (2y-x)/(y+2x)
    numerator = 2*Y - X
    denominator = Y + 2*X

    angles = np.zeros_like(numerator, dtype=float)

    # A small epsilon to check for values close to zero
    epsilon = 1e-6

    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            den = denominator[i, j]
            num = numerator[i, j]

            # Handle division by zero for vertical slopes
            if abs(den) < epsilon:
                # If both numerator and denominator are near zero (at origin), 
                # the field shows a vertical segment, so we'll approximate it as such.
                # If only denominator is near zero, it's a true vertical tangent.
                angles[i, j] = np.pi / 2 
            else:
                current_slope = num / den
                angles[i, j] = np.arctan(current_slope)

    # Plotting the direction field
    fig, ax = plt.subplots(figsize=(8, 6))

    # Length of the segments
    L = 0.5 # Adjust segment length for visual clarity

    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            x_coord, y_coord = X[i, j], Y[i, j]
            angle = angles[i, j]

            # Calculate start and end points of the segment
            dx = L * np.cos(angle) / 2
            dy = L * np.sin(angle) / 2

            ax.plot([x_coord - dx, x_coord + dx], [y_coord - dy, y_coord + dy], 'k-', linewidth=0.8)

    # Add axes and grid
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.set_xticks(np.arange(x_min, x_max + 1, 1))
    ax.set_yticks(np.arange(y_min, y_max + 1, 1))
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.set_xlabel('x')
    ax.set_ylabel('y', rotation=0, labelpad=10)

    # Set limits and aspect ratio to match the image
    ax.set_xlim(x_min - 0.5, x_max + 0.5)
    ax.set_ylim(y_min - 0.5, y_max + 0.5)
    ax.set_aspect('equal', adjustable='box') 

    plt.title('Direction Field for dy/dx = (2y-x)/(y+2x)')
    plt.tight_layout()

    # Save plot to a BytesIO object
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig) 
    
    return img_base64