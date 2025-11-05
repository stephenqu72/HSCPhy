import numpy as np
import plotly.graph_objects as go

def generate_plot():
    # Define the function y = sqrt(16 - (x+1)^2)
    # This is the upper semi-circle of (x+1)^2 + y^2 = 16
    # Center (-1, 0), Radius 4
    x_values = np.linspace(-5, 3, 400)
    y_values = np.sqrt(16 - (x_values + 1)**2)

    # Create the plot for the original curve
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines', name='y = sqrt(16-(x+1)^2)'))
    fig.add_trace(go.Scatter(x=x_values, y=-y_values, mode='lines', name='y = -sqrt(16-(x+1)^2)', line=dict(dash='dot'))) # Lower half for visualization reference

    # Add x-axis
    fig.add_trace(go.Scatter(x=[-5, 3], y=[0, 0], mode='lines', name='x-axis (Rotation Axis)', line=dict(color='red', width=2)))

    # Add points for x-intercepts
    fig.add_trace(go.Scatter(x=[-5, 3], y=[0, 0], mode='markers', name='x-intercepts', 
                             marker=dict(size=8, color='purple')))

    # Add center of the circle
    fig.add_trace(go.Scatter(x=[-1], y=[0], mode='markers', name='Circle Center',
                             marker=dict(size=8, color='green', symbol='circle')))

    fig.update_layout(
        title="Curve $y = \sqrt{16-(x+1)^2}$ and its Rotation Axis",
        xaxis_title="x",
        yaxis_title="y",
        hovermode="x unified",
        yaxis_scaleanchor="x", # Make sure scales are equal for circular shape
        yaxis_scaleratio=1,
        showlegend=True,
        template="plotly_white"
    )
    return fig