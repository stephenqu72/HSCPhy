import plotly.graph_objects as go
import numpy as np
import math

def generate_plot():
    # Define the range for x
    x_vals = np.linspace(0, np.pi/2, 200)

    # Calculate y values for y=x and y=sin(x)
    y_x = x_vals
    y_sin_x = np.sin(x_vals)

    # Create the figure
    fig = go.Figure()

    # Add the curve y = x
    fig.add_trace(go.Scatter(x=x_vals, y=y_x, mode='lines', name='y=x',
                             line=dict(color='blue', width=2)))

    # Add the curve y = sin(x)
    fig.add_trace(go.Scatter(x=x_vals, y=y_sin_x, mode='lines', name='y=sin(x)',
                             line=dict(color='red', width=2)))

    # Add shaded region R
    x_fill = np.concatenate([x_vals, x_vals[::-1]])
    y_fill = np.concatenate([y_x, y_sin_x[::-1]])
    fig.add_trace(go.Scatter(x=x_fill, y=y_fill, fill='toself',
                             fillcolor='rgba(169, 169, 169, 0.7)', # Grey with transparency
                             line_color='rgba(255,255,255,0)', # Invisible line for boundary
                             showlegend=False, name='Region R'))

    # Add the vertical dashed line x = pi/2
    x_pi_half = np.pi/2
    y_pi_half_upper = x_pi_half
    # y_pi_half_lower = np.sin(x_pi_half) # which is 1
    fig.add_trace(go.Scatter(x=[x_pi_half, x_pi_half], y=[0, y_pi_half_upper],
                             mode='lines', line=dict(dash='dash', color='black', width=1),
                             showlegend=False))

    # Annotations for labels and origin (adjusted for better placement)
    fig.add_annotation(x=np.pi/2 + 0.1, y=np.pi/2 + 0.1, text="y = x", showarrow=False, font=dict(size=12))
    fig.add_annotation(x=np.pi/2 + 0.1, y=np.sin(np.pi/2) - 0.1, text="y = sin x", showarrow=False, font=dict(size=12))
    # R label placed in the middle of the shaded area
    fig.add_annotation(x=(0 + np.pi/2)/2, y=(( (0 + np.pi/2)/2 + np.sin((0 + np.pi/2)/2) ) / 2) + 0.1, text="R", showarrow=False, font=dict(size=14, color="black", weight='bold'))
    fig.add_annotation(x=0, y=0, text="O", showarrow=False, xanchor='right', yanchor='top', font=dict(size=12))

    # Update layout for better appearance
    fig.update_layout(
        title='Area of Region R',
        xaxis_title='x',
        yaxis_title='y',
        xaxis_range=[-0.2, np.pi * 0.8], # Extend range slightly for labels
        yaxis_range=[-0.2, np.pi/2 + 0.5], # Extend range slightly
        template='plotly_white',
        showlegend=False,
        # Custom ticks
        xaxis=dict(
            tickmode='array',
            tickvals=[0, 1, np.pi/2, 2],
            ticktext=['0', '1', r'$\frac{\pi}{2}$', '2']
        ),
        yaxis=dict(
            tickmode='array',
            tickvals=[0, 1, 2],
            ticktext=['0', '1', '2']
        ),
        # Remove grid lines for a cleaner look
        xaxis_showgrid=False,
        yaxis_showgrid=False
    )

    return fig