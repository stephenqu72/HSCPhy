import plotly.graph_objects as go
import numpy as np

def generate_plot():
    t = np.linspace(0, 3.5, 100)
    s = t**2  # Illustrative example for constant acceleration (s = 0.5 * a * t^2 if u=0)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=s, mode='lines', name='Displacement', line=dict(color='blue', width=2)))

    # Illustrative points P and Q (consistent with the visual representation)
    p_time = 1.8
    p_displacement = p_time**2
    q_time = 3.0
    q_displacement = q_time**2

    fig.add_trace(go.Scatter(x=[p_time], y=[p_displacement], mode='markers', marker=dict(size=8, color='red'), name='Point P'))
    fig.add_trace(go.Scatter(x=[q_time], y=[q_displacement], mode='markers', marker=dict(size=8, color='green'), name='Point Q'))

    # Add dotted lines for P and Q as in the original image
    fig.add_trace(go.Scatter(x=[0, p_time, p_time], y=[p_displacement, p_displacement, 0], 
                             mode='lines', line=dict(dash='dot', color='grey'), showlegend=False))
    fig.add_trace(go.Scatter(x=[0, q_time, q_time], y=[q_displacement, q_displacement, 0], 
                             mode='lines', line=dict(dash='dot', color='grey'), showlegend=False))

    fig.update_layout(
        title='Illustrative Displacement-Time Graph',
        xaxis_title='Time (s)',
        yaxis_title='Displacement (m)',
        hovermode='x unified',
        showlegend=True,
        template='plotly_white'
    )
    return fig