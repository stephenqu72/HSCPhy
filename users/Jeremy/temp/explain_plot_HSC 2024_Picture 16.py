import plotly.graph_objects as go
import numpy as np
import base64
from io import BytesIO

def generate_plot():
    # Generate data for the radius (r)
    r_values = np.linspace(1, 5, 100) # Radius from 1 cm to 5 cm

    # Calculate dr/dt using the derived formula: dr/dt = 5 / (2 * pi * r^2)
    dr_dt_values = 5 / (2 * np.pi * r_values**2)

    # Create the plot
    fig = go.Figure(
        data=[go.Scatter(x=r_values, y=dr_dt_values, mode='lines', name='dr/dt vs r')],
        layout=go.Layout(
            title='Rate of Change of Radius (dr/dt) vs. Radius (r)',
            xaxis_title='Radius r (cm)',
            yaxis_title='Rate of Change of Radius dr/dt (cm/s)',
            hovermode='x unified'
        )
    )
    return fig

# To make the code runnable and generate base64 output if needed:
# fig = generate_plot()
# fig_bytes = fig.to_image(format='png') # or 'json' for data table
# base64_image = base64.b64encode(fig_bytes).decode('utf-8')