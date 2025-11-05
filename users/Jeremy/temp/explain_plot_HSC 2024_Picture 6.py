import plotly.graph_objects as go
import numpy as np

def generate_plot():
    x_vals = np.linspace(0, 2 * np.pi, 500)
    y_sin_abs = np.abs(np.sin(4 * x_vals))
    y_one = np.ones_like(x_vals)

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=x_vals, y=y_sin_abs, mode='lines', name='|sin(4x)|', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=x_vals, y=y_one, mode='lines', name='y=1', line=dict(color='red', dash='dash')))

    # Calculate and mark the solutions
    # General solutions for |sin(u)| = 1 is u = pi/2 + k*pi
    # For u = 4x, range for u is [0, 8pi]
    # pi/2 + k*pi in [0, 8pi] => 0 <= 1/2 + k <= 8 => -1/2 <= k <= 15/2
    # So k = 0, 1, 2, 3, 4, 5, 6, 7
    solutions_4x = np.array([np.pi/2 + k*np.pi for k in range(8)])
    solutions_x = solutions_4x / 4
    solutions_y = np.ones_like(solutions_x)

    fig.add_trace(go.Scatter(x=solutions_x, y=solutions_y, mode='markers', name='Solutions', 
                             marker=dict(color='green', size=8, symbol='x')))

    fig.update_layout(
        title='Graph of |sin(4x)| and y=1 for x in [0, 2π]',
        xaxis_title='x', 
        yaxis_title='y',
        xaxis=dict(tickvals=[0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
                   ticktext=['0', 'π/2', 'π', '3π/2', '2π']),
        yaxis=dict(range=[-0.1, 1.1]),
        showlegend=True
    )
    return fig