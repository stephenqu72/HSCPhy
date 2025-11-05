import matplotlib.pyplot as plt
import numpy as np

def generate_plot():
    fig, ax = plt.subplots(figsize=(7, 6))

    # PPC curve (using a simple function for demonstration)
    x_values = np.linspace(0, 10, 100)
    y_values = np.sqrt(100 - x_values**2) # Quarter circle for illustrative PPC
    ax.plot(x_values, y_values, label='PPC', color='black')

    # Point Y
    y_capital_Y = 8
    x_consumer_Y = np.sqrt(100 - y_capital_Y**2)
    ax.plot(x_consumer_Y, y_capital_Y, 'o', color='black', markersize=8, label='Y')
    ax.axvline(x=x_consumer_Y, linestyle='--', color='gray', linewidth=0.8)
    ax.axhline(y=y_capital_Y, linestyle='--', color='gray', linewidth=0.8)
    ax.text(x_consumer_Y + 0.3, y_capital_Y + 0.3, 'Y', fontsize=12, ha='left', va='bottom')

    # Point X
    x_consumer_X = 8
    y_capital_X = np.sqrt(100 - x_consumer_X**2)
    ax.plot(x_consumer_X, y_capital_X, 'o', color='black', markersize=8, label='X')
    ax.axvline(x=x_consumer_X, linestyle='--', color='gray', linewidth=0.8)
    ax.axhline(y=y_capital_X, linestyle='--', color='gray', linewidth=0.8)
    ax.text(x_consumer_X + 0.3, y_capital_X + 0.3, 'X', fontsize=12, ha='left', va='bottom')

    ax.set_xlabel('Consumer goods', fontsize=12)
    ax.set_ylabel('Capital goods', fontsize=12)
    ax.set_title('Production Possibility Curve', fontsize=14)
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 10.5)
    ax.grid(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    # Adding an arrow for the x-axis and y-axis
    ax.plot(10.5, 0, '>', color='black', transform=ax.get_yaxis_transform(), clip_on=False, markersize=8)
    ax.plot(0, 10.5, '^', color='black', transform=ax.get_xaxis_transform(), clip_on=False, markersize=8)


    plt.tight_layout()
    return fig

# The function `generate_plot()` is defined and will return a Matplotlib figure object.