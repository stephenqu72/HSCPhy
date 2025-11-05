import plotly.graph_objects as go
import numpy as np
from scipy.stats import norm

def generate_plot():
    # Define the range for Z values
    z_min = -3
    z_max = 3
    z = np.linspace(z_min, z_max, 500)
    pdf = norm.pdf(z)

    # Calculate z-scores for shading from the detailed explanation.
    # We use the rounded z-scores as per table lookup.
    z1_shade = -1.63
    z2_shade = -0.54

    # Create the figure
    fig = go.Figure()

    # Add the normal distribution curve
    fig.add_trace(go.Scatter(x=z, y=pdf, mode='lines', name='Standard Normal PDF', line=dict(color='blue')))

    # Create the shaded area for P(z1_shade <= Z <= z2_shade)
    z_shaded = z[(z >= z1_shade) & (z <= z2_shade)]
    pdf_shaded = pdf[(z >= z1_shade) & (z <= z2_shade)]

    # Only add fill if there's a valid range to shade
    if len(z_shaded) > 1:
        fig.add_trace(go.Scatter(
            x=np.concatenate([[z_shaded[0]], z_shaded, [z_shaded[-1]]]),
            y=np.concatenate([[0], pdf_shaded, [0]]),
            fill='toself',
            fillcolor='rgba(255, 0, 0, 0.3)',
            line_color='rgba(255, 0, 0, 0)',
            name=f'Area for P({z1_shade:.2f} <= Z <= {z2_shade:.2f})'
        ))

    # Add labels for the z-scores
    fig.add_vline(x=z1_shade, line_width=1, line_dash="dash", line_color="green", annotation_text=f"z1={z1_shade:.2f}", annotation_position="top left")
    fig.add_vline(x=z2_shade, line_width=1, line_dash="dash", line_color="green", annotation_text=f"z2={z2_shade:.2f}", annotation_position="top right")

    # Update layout
    fig.update_layout(
        title='Standard Normal Distribution with Shaded Probability Region',
        xaxis_title='Z-score',
        yaxis_title='Probability Density',
        showlegend=True,
        hovermode='x unified'
    )
    return fig