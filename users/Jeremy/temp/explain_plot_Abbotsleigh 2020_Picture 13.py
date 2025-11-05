import plotly.graph_objects as go
import numpy as np

def generate_plot():
    theta = np.linspace(0, np.pi, 500)
    y = np.sin(4 * theta) + np.sqrt(3) * np.cos(4 * theta)

    # Solutions found in radians
    solutions_theta = np.array([np.pi/6, 5*np.pi/12, 2*np.pi/3, 11*np.pi/12])
    solutions_y = np.zeros_like(solutions_theta)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=theta, y=y, mode='lines', name='y = sin(4θ) + √3 cos(4θ)'))
    fig.add_trace(go.Scatter(x=[0, np.pi], y=[0, 0], mode='lines', name='y = 0', line=dict(color='grey', dash='dash')))
    fig.add_trace(go.Scatter(x=solutions_theta, y=solutions_y, mode='markers', name='Solutions', 
                             marker=dict(color='red', size=8, line=dict(width=1, color='DarkRed'))))

    # Custom x-axis ticks for better readability of solutions
    tick_vals = [0, np.pi/6, 5*np.pi/12, 2*np.pi/3, 11*np.pi/12, np.pi]
    tick_text = ['0', 'π/6', '5π/12', '2π/3', '11π/12', 'π']

    fig.update_layout(
        title='Solutions for sin(4θ) + √3 cos(4θ) = 0',
        xaxis_title='θ (radians)',
        yaxis_title='Value of expression',
        hovermode='x unified',
        template='plotly_white',
        xaxis=dict(
            tickmode='array',
            tickvals=tick_vals,
            ticktext=tick_text,
            range=[0, np.pi]
        ),
        yaxis_range=[-2.1, 2.1],
        showlegend=True
    )
    return fig