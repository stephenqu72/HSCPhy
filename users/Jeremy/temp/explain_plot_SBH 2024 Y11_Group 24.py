import numpy as np
import matplotlib.pyplot as plt

def generate_plot():
    x_values = np.linspace(0, 4.0, 500) # One complete cycle of wave A

    # Wave A: λ_A = 4.0, Amplitude A_A = 4.5. Starts at (0,0). y_A(x) = A_A * sin( (2*pi/λ_A) * x )
    y_A_values = 4.5 * np.sin((np.pi / 2.0) * x_values)

    # Wave B: λ_B = 2.0, Amplitude A_B = 6.0. Starts at (0, ~-5.8, derived as -6.0cos(0)). y_B(x) = -A_B * cos( (2*pi/λ_B) * x )
    y_B_values = -6.0 * np.cos(np.pi * x_values)

    # Superposition: y_resultant = y_A + y_B
    y_resultant_values = y_A_values + y_B_values

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(x_values, y_A_values, color='blue', linestyle='-', label='Wave A')
    ax.plot(x_values, y_B_values, color='green', linestyle='--', label='Wave B')
    ax.plot(x_values, y_resultant_values, color='red', linestyle=':', linewidth=3, label='Resultant Wave (A+B)')

    ax.grid(True, linestyle=':', alpha=0.7)
    ax.set_xlabel('dist. [$10^{-2}$ m]')
    ax.set_ylabel('x [$10^{-2}$ m]')
    ax.set_title('Superposition of Waves A and B (for one cycle of A)')
    ax.legend()

    ax.set_xlim(0, 4.0)
    ax.set_ylim(-10, 11) # Adjusted to show the actual maximum of 10.5 for the resultant wave
    
    ax.set_xticks(np.arange(0, 4.1, 0.5), minor=True)
    ax.set_xticks(np.arange(0, 4.1, 1.0))
    ax.set_yticks(np.arange(-10, 10.1, 1), minor=True)
    ax.set_yticks(np.arange(-10, 10.1, 5))

    return fig