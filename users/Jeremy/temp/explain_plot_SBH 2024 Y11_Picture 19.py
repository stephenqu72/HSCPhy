import plotly.graph_objects as go
import numpy as np

def generate_plot():
    # In this scenario, the change in momentum (impulse) is constant.
    # Impulse = Average Force * time taken (F_avg * Δt)
    # Also, Impulse = Change in momentum (Δp = m * Δv)
    # So, F_avg * Δt = m * Δv (constant)
    # F_avg = (m * Δv) / Δt
    # Let's assume m * Δv = 30 (arbitrary constant for visualization)
    
    delta_t = np.linspace(0.1, 10, 200)  # Time taken from 0.1s to 10s
    constant_momentum_change = 30 # Represents m * Δv, an arbitrary constant
    F_avg = constant_momentum_change / delta_t

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=delta_t, y=F_avg, mode='lines', name='Average Force vs. Time'))

    fig.update_layout(
        title='Average Force vs. Time Taken to Stop',
        xaxis_title='Time taken to stop (Δt)',
        yaxis_title='Average Force (F_avg)',
        font=dict(size=12),
        template='plotly_white'
    )
    return fig