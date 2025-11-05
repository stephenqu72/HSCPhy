import plotly.graph_objects as go
import numpy as np

def generate_plot():
    # Define the domain
    x_values = np.linspace(-0.5, 0.5, 100)
    # The function evaluates to y = pi for all x in the domain
    y_values = np.full_like(x_values, np.pi)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines', name='y = 2cos⁻¹(2x) + 2sin⁻¹(2x)'))

    # Add specific points for clarity
    fig.add_trace(go.Scatter(x=[-0.5, 0.5], y=[np.pi, np.pi], mode='markers', marker=dict(size=8, color='red'), name='Endpoints'))

    fig.update_layout(
        title='Graph of y = 2cos⁻¹(2x) + 2sin⁻¹(2x)',
        xaxis_title='x',
        yaxis_title='y',
        yaxis_range=[np.pi - 0.5, np.pi + 0.5], # Zoom in around pi
        hovermode='x unified'
    )
    return fig