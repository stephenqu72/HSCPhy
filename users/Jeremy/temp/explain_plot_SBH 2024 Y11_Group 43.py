import plotly.graph_objects as go
import numpy as np

def generate_plot():
    # Data points from the image (epsilon [V], B [x 10^-4 T])
    epsilon_data = [1.5, 3.0, 4.25, 5.0, 7.0]
    B_data_raw = [0.7, 1.4, 1.7, 2.25, 2.75]

    # Points used for the line of best fit from the image (extrapolated)
    # The line appears to go from (0, 0.2) to (7, 2.75) in the B_raw scale.
    epsilon_line = np.array([0.0, 7.0])
    B_line_raw = np.array([0.2, 2.75])
    
    # Extrapolated dashed line from the image (between 0 and approx 1V)
    epsilon_dashed = np.array([0.0, 1.0])
    B_dashed_raw = np.array([0.2, 0.5]) 

    fig = go.Figure()

    # Add data points
    fig.add_trace(go.Scatter(
        x=epsilon_data,
        y=B_data_raw, 
        mode='markers',
        marker=dict(symbol='x', size=10, color='black'),
        name='Experimental Data'
    ))

    # Add solid line of best fit
    fig.add_trace(go.Scatter(
        x=epsilon_line,
        y=B_line_raw, 
        mode='lines',
        line=dict(color='red', width=2),
        name='Line of Best Fit'
    ))

    # Add extrapolated dashed line
    fig.add_trace(go.Scatter(
        x=epsilon_dashed,
        y=B_dashed_raw, 
        mode='lines',
        line=dict(color='red', width=2, dash='dash'),
        showlegend=False # This is part of the same line, just dashed
    ))

    fig.update_layout(
        #title='Magnetic Field Strength vs. EMF for a Solenoid', # Removed as it's not in the original
        xaxis_title='ε [V]',
        yaxis_title='B [× 10⁻⁴ T]', 
        hovermode='x unified',
        font=dict(
            family="Arial, sans-serif",
            size=12,
            color="black"
        ),
        margin=dict(l=40, r=40, b=40, t=40),
        yaxis=dict(
            range=[0, 3.0], 
            tickvals=[0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0],
            gridcolor='lightgray', # Add grid to match image
            griddash='dot'
        ),
        xaxis=dict(
            range=[0, 8.0],
            tickvals=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            gridcolor='lightgray', # Add grid to match image
            griddash='dot'
        ),
        showlegend=True,
        legend=dict(
            x=0.01,
            y=0.99,
            xanchor='left',
            yanchor='top'
        )
    )

    return fig