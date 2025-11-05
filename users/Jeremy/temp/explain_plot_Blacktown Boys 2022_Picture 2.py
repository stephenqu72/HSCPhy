import plotly.graph_objects as go
import numpy as np

def generate_plot():
    x_min, x_max = -3, 6
    y_min, y_max = -3, 3

    # Create a grid of points
    x_coords = np.arange(x_min, x_max + 1, 0.5) # x-coordinates for the grid
    y_coords = np.arange(y_min, y_max + 1, 0.5) # y-coordinates for the grid
    X, Y = np.meshgrid(x_coords, y_coords) # Create 2D arrays for x and y at each grid point

    # Calculate the slopes for dy/dx = -x/2
    # For a slope field, we represent the slope dy/dx = m as a vector (u,v) where v/u = m.
    # A common choice is u=1 and v=m, then normalize for uniform arrow length.
    U = np.ones_like(X) # dx component (set to 1 for simplicity and then normalize)
    V = -X / 2          # dy component (from the differential equation dy/dx = -x/2)

    # Normalize vectors to a consistent length for better visualization
    lengths = np.sqrt(U**2 + V**2)
    U_norm = U / lengths
    V_norm = V / lengths

    fig = go.Figure() # Initialize Plotly figure

    # Define the length of each arrow segment for drawing
    arrow_length = 0.25 

    # Iterate through each grid point to draw a slope segment
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            x_start = X[i, j]
            y_start = Y[i, j]
            # Calculate end point of the arrow segment based on normalized vector and arrow_length
            x_end = x_start + arrow_length * U_norm[i, j]
            y_end = y_start + arrow_length * V_norm[i, j]

            # Add the line segment to the figure
            fig.add_trace(go.Scatter(
                x=[x_start, x_end],
                y=[y_start, y_end],
                mode='lines',
                line=dict(color='gray', width=1), # Styling for the line segments
                hoverinfo='none', # No hover information needed for these segments
                showlegend=False # Do not show this trace in the legend
            ))

    # Update layout for title, axis labels, ranges, and aspect ratio
    fig.update_layout(
        title=r'Slope Field for $\frac{dy}{dx} = -\frac{x}{2}$', # Title with LaTeX math
        xaxis_title='x',
        yaxis_title='y',
        xaxis=dict(range=[x_min, x_max + 1], dtick=1), # Set x-axis range and major tick interval
        yaxis=dict(range=[y_min, y_max], dtick=1), # Set y-axis range and major tick interval
        yaxis_scaleanchor="x", # Ensure equal scaling for x and y axes
        yaxis_scaleratio=1,
        plot_bgcolor='white' # Set background color to white
    )
    # Add grid lines for better readability
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')

    return fig