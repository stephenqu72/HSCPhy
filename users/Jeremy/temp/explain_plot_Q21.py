import plotly.graph_objects as go
import numpy as np

def generate_plot():
    # Define distance range for plotting in units of 10^-2 m
    # Extended to 6.0 for full context of original graph
    dist_10_minus_2_m = np.linspace(0, 6.0, 500)

    # Wave A (solid blue line)
    # Amplitude A_A = 4.0 (in units of 10^-2 m)
    # Wavelength lambda_A = 4.0 (in units of 10^-2 m)
    # Function: y_A = A_A * sin(2*pi*dist/lambda_A)
    y_A = 4.0 * np.sin(2 * np.pi * dist_10_minus_2_m / 4.0)

    # Wave B (dashed green line)
    # Amplitude A_B = 6.0 (in units of 10^-2 m)
    # Wavelength lambda_B = 2.0 (in units of 10^-2 m)
    # From the graph, wave B peaks at 0.5, 2.5 and troughs at 1.5, 3.5. Zero crossings at 1.0, 2.0, 3.0, 4.0.
    # This pattern matches a cosine function shifted to have its peak at dist = 0.5.
    # Function: y_B = A_B * cos( (2*pi/lambda_B) * (dist - dist_peak) )
    # y_B = 6.0 * np.cos( (2 * np.pi / 2.0) * (dist_10_minus_2_m - 0.5) )
    # Note: This function accurately models the shape of wave B from dist=0.5 onwards. 
    # The graph's starting point at dist=0, y_B approx -5, is an anomaly if the wave is a perfect sinusoid.
    # For the plot, the mathematically consistent sinusoidal function based on amplitude and period is used.
    y_B = 6.0 * np.cos(np.pi * (dist_10_minus_2_m - 0.5))

    # Calculate superposition for one complete cycle of wave A (from dist=0 to dist=4.0)
    dist_superposition_range = dist_10_minus_2_m[dist_10_minus_2_m <= 4.0]
    y_A_superposition = y_A[dist_10_minus_2_m <= 4.0]
    y_B_superposition = y_B[dist_10_minus_2_m <= 4.0]
    y_superposition = y_A_superposition + y_B_superposition

    # Create the plot
    fig = go.Figure()

    # Plot Wave A
    fig.add_trace(go.Scatter(x=dist_10_minus_2_m, y=y_A,
                             mode='lines',
                             name='Wave A',
                             line=dict(color='blue', width=2),
                             showlegend=True))

    # Plot Wave B
    fig.add_trace(go.Scatter(x=dist_10_minus_2_m, y=y_B,
                             mode='lines',
                             name='Wave B',
                             line=dict(color='green', width=2, dash='dash'),
                             showlegend=True))

    # Plot Superposition (Standing Wave) for one cycle of Wave A
    fig.add_trace(go.Scatter(x=dist_superposition_range, y=y_superposition,
                             mode='lines',
                             name='Superposed Wave (Standing Wave at this instant)',
                             line=dict(color='red', width=3, dash='solid'),
                             showlegend=True))

    # Update layout for better readability and mimic original graph style
    fig.update_layout(
        title='Superposition of Waves A and B',
        xaxis_title='Distance [10<sup>-2</sup> m]',
        yaxis_title='Displacement x [10<sup>-2</sup> m]',
        xaxis=dict(range=[0, 6.0], dtick=1.0, showgrid=True, gridwidth=1, gridcolor='LightGray'),
        yaxis=dict(range=[-10, 10], dtick=5.0, showgrid=True, gridwidth=1, gridcolor='LightGray'),
        hovermode="x unified",
        legend=dict(x=0.01, y=0.99, bgcolor='rgba(255,255,255,0.7)', bordercolor='rgba(0,0,0,0.5)', borderwidth=1)
    )
    # Add minor grid lines for every 0.5 on x-axis and 1.0 on y-axis, similar to the image
    fig.update_xaxes(minor=dict(dtick=0.5, showgrid=True, gridwidth=0.5, gridcolor='LightGray'))
    fig.update_yaxes(minor=dict(dtick=1.0, showgrid=True, gridwidth=0.5, gridcolor='LightGray'))

    return fig