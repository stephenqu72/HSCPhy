import matplotlib.pyplot as plt
import numpy as np

def generate_plot():
    fig, ax = plt.subplots(figsize=(8, 8))

    # Set up the Argand diagram grid and axes
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel('Re(z)')
    ax.set_ylabel('Im(z)')
    ax.set_title('Argand diagram for Question 14(c)')
    
    # Set limits based on the original diagram (radius 3 circles visible)
    ax.set_xlim([-3.5, 3.5])
    ax.set_ylim([-3.5, 3.5])

    # Draw grid lines (similar to the provided diagram)
    for i in range(1, 4):
        # Circles
        circle = plt.Circle((0, 0), i, color='lightgrey', linestyle='--', fill=False, zorder=0)
        ax.add_artist(circle)
    # Radial lines (24 lines as per the diagram)
    for angle in np.linspace(0, 2*np.pi, 24, endpoint=False): # 24 lines in the diagram
        ax.plot([0, 3*np.cos(angle)], [0, 3*np.sin(angle)], color='lightgrey', linestyle='--', zorder=0)

    # Draw main axes
    ax.axhline(0, color='black', linewidth=1, zorder=1)
    ax.axvline(0, color='black', linewidth=1, zorder=1)

    # Add axis ticks and labels
    ax.set_xticks(np.arange(-3, 4, 1))
    ax.set_yticks(np.arange(-3, 4, 1))

    # --- Part (c)(i): Sketch A = {z : z z_bar = 4} ---
    # This is |z|^2 = 4, so |z|=2. A circle with radius 2 centered at the origin.
    circle_A = plt.Circle((0, 0), 2, color='blue', linestyle='-', linewidth=2, fill=False, label='$A: |z|=2$', zorder=2)
    ax.add_artist(circle_A)
    # Label A near the circle
    ax.text(2.1, 0.1, 'A', color='blue', fontsize=12, ha='left')

    # --- Part (c)(ii): Sketch B = {z : |z| = |z - 2cis(pi/4)|} ---
    # This is the perpendicular bisector of the line segment from 0 to 2cis(pi/4).
    # 2cis(pi/4) = 2(cos(pi/4) + i sin(pi/4)) = 2(sqrt(2)/2 + i sqrt(2)/2) = sqrt(2) + i*sqrt(2)
    # The line is x + y = sqrt(2).
    # Intercepts: (sqrt(2), 0) and (0, sqrt(2)).
    sqrt2 = np.sqrt(2)
    
    # Generate line points, extending beyond the circle for full sketch
    line_x = np.array([-1.5, 3]) # Extend line for visibility
    line_y = sqrt2 - line_x
    ax.plot(line_x, line_y, color='green', linestyle='-', linewidth=2, label='$B: x+y=\sqrt{2}$', zorder=2)
    
    # Label B near the line
    ax.text(1.5, 0.2, 'B', color='green', fontsize=12, ha='left')

    # Label axis intercepts for line B
    ax.plot(sqrt2, 0, 'go') # mark intercept
    ax.plot(0, sqrt2, 'go') # mark intercept
    ax.text(sqrt2 + 0.1, -0.1, '($\sqrt{2}, 0$)', color='green', fontsize=10, ha='left', va='top')
    ax.text(-0.1, sqrt2 + 0.1, '($0, \sqrt{2}$)', color='green', fontsize=10, ha='right', va='bottom')

    # --- Part (c)(iii): Shade the region {z : z z_bar <= 4} INTERSECT {z : Re(z) + Im(z) >= sqrt(2)} ---
    # This is |z| <= 2 AND x + y >= sqrt(2).
    # The line is x + y = sqrt(2). The region x+y >= sqrt(2) is above and to the right of the line.
    # The region |z| <= 2 is the interior of circle A.
    # The shaded region is the major segment defined by the chord x+y=sqrt(2) and the circle |z|=2.

    # Intersection points of x^2+y^2=4 and x+y=sqrt(2)
    x_P1 = (sqrt2 - np.sqrt(6)) / 2
    y_P1 = (sqrt2 + np.sqrt(6)) / 2
    x_P2 = (sqrt2 + np.sqrt(6)) / 2
    y_P2 = (sqrt2 - np.sqrt(6)) / 2

    # Angles for these points for the major arc (counter-clockwise from P1 to P2)
    theta_P1 = np.arctan2(y_P1, x_P1) # Q2 angle: ~105 degrees (7pi/12)
    theta_P2 = np.arctan2(y_P2, x_P2) # Q4 angle: ~-15 degrees (-pi/12)

    # Adjust theta_P2 to be greater than theta_P1 for a counter-clockwise major arc span
    if theta_P2 < theta_P1:
        theta_P2 += 2 * np.pi # This makes theta_P2 ~345 degrees (23pi/12)
    
    # Generate points along the major arc
    # The arc starts at P1 (theta_P1) and goes counter-clockwise to P2 (theta_P2)
    arc_angles = np.linspace(theta_P1, theta_P2, 100)
    arc_x = 2 * np.cos(arc_angles)
    arc_y = 2 * np.sin(arc_angles)

    # Shade the region. The fill function automatically closes the polygon
    # by connecting the last point to the first. This creates the major segment.
    ax.fill(arc_x, arc_y, color='orange', alpha=0.5, zorder=1, label='Shaded Region')
    
    # Return the figure object
    return fig