import matplotlib.pyplot as plt

def generate_plot():
    # Define coordinates for A, B, C for visualization purposes
    A = (0, 6)
    B = (-4, 0)
    C = (8, 0)

    # Calculate D: BD = (1/3)BC => D divides BC in ratio 1:2
    # Position vector OD = (2*OB + 1*OC) / (1+2) = (2/3)OB + (1/3)OC
    D = ((2/3)*B[0] + (1/3)*C[0], (2/3)*B[1] + (1/3)*C[1])

    # Calculate M: M is midpoint of AD
    # Position vector OM = (OA + OD) / 2
    M = ((A[0] + D[0])/2, (A[1] + D[1])/2)

    # Calculate X: AX = (1/4)AC => X divides AC in ratio 1:3
    # Position vector OX = (3*OA + 1*OC) / (3+1) = (3/4)OA + (1/4)OC
    X = ((3/4)*A[0] + (1/4)*C[0], (3/4)*A[1] + (1/4)*C[1])

    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot points
    points = {'A': A, 'B': B, 'C': C, 'D': D, 'M': M, 'X': X}
    for label, (x, y) in points.items():
        ax.plot(x, y, 'o', markersize=6, color='blue')
        ax.text(x + 0.2, y + 0.2, label, fontsize=12, color='darkblue')

    # Plot lines of triangle ABC
    ax.plot([A[0], B[0]], [A[1], B[1]], 'k-', linewidth=1)
    ax.plot([B[0], C[0]], [B[1], C[1]], 'k-', linewidth=1)
    ax.plot([C[0], A[0]], [C[1], A[1]], 'k-', linewidth=1)

    # Plot AD
    ax.plot([A[0], D[0]], [A[1], D[1]], 'k-', linewidth=1)

    # Plot BX (to show collinearity, M lies on this line)
    ax.plot([B[0], X[0]], [B[1], X[1]], 'r--', linewidth=2, label='Line B-M-X')

    # Add labels and title
    ax.set_title("Vector Diagram for Triangle ABC", fontsize=14)
    ax.set_xlabel("x-coordinate", fontsize=10)
    ax.set_ylabel("y-coordinate", fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_aspect('equal', adjustable='box')
    ax.legend()

    # Adjust limits slightly for better visualization
    all_x = [p[0] for p in points.values()]
    all_y = [p[1] for p in points.values()]
    ax.set_xlim(min(all_x) - 1, max(all_x) + 1)
    ax.set_ylim(min(all_y) - 1, max(all_y) + 1)

    return fig