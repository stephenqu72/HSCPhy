import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import PchipInterpolator
import base64
import io

def generate_plot():
    # Define characteristic points for f(x) based on the image and description
    # These points are chosen to approximate the given sketch of f(x)
    x_key_points = np.array([-4, -2, 0, 1, 2, 3, 4])
    # y_key_points are derived from image analysis and calculation for the 0 <= x <= 3 segment
    # f(-4) = 4 (approx from graph)
    # f(-2) = 2.7 (approx from graph, ensures decreasing convex shape)
    # f(0) = 2 (given)
    # f(1) = 0 (given)
    # f(2) = -2/3 approx -0.67 (calculated local minimum for the quadratic between 0 and 3, f(x)=(2/3)x^2-(8/3)x+2)
    # f(3) = 0 (given)
    # f(4) = 1.5 (approx from graph, ensuring increasing behavior)
    y_key_points = np.array([4, 2.7, 2, 0, -0.67, 0, 1.5]) 

    # Create an interpolator for f(x) to generate a smooth curve.
    # PchipInterpolator is good for preserving monotonicity and shape without overshooting.
    f_interpolator = PchipInterpolator(x_key_points, y_key_points)

    # Generate x values for plotting within the domain [-4, 4]
    x_vals = np.linspace(-4, 4, 500)
    # Calculate corresponding y values for f(x)
    y_vals = f_interpolator(x_vals)

    # --- Initialize Plotly Figure ---
    fig = go.Figure()

    # Add the original f(x) as a dotted light gray line for reference
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name='y = f(x) (Original)', line=dict(color='lightgray', dash='dot', width=1.5)))

    # --- (i) Sketch y = f(|x|) ---
    # The graph for y = f(|x|) is obtained by:
    # 1. Keeping the part of f(x) for x >= 0.
    # 2. Reflecting this part across the y-axis to get the graph for x < 0.
    x_pos_part = x_vals[x_vals >= 0]
    y_pos_part = f_interpolator(x_pos_part)
    
    # Reflect the positive x-part
    x_reflected_part = -x_pos_part[::-1] # Reverse and negate x for reflection
    y_reflected_part = y_pos_part[::-1] # Corresponding y-values also reversed

    # Combine the reflected part and the original positive x-part
    x_f_abs_x = np.concatenate((x_reflected_part, x_pos_part))
    y_f_abs_x = np.concatenate((y_reflected_part, y_pos_part))

    fig.add_trace(go.Scatter(x=x_f_abs_x, y=y_f_abs_x, mode='lines', name='y = f(|x|)', line=dict(color='blue', width=2)))

    # --- (ii) Sketch y = 1/f(x) ---
    # Key features:
    # - Vertical asymptotes where f(x) = 0 (at x=1 and x=3).
    # - Reciprocal of y-values.
    # - Local maxima of f(x) become local minima of 1/f(x) and vice-versa.
    
    # Handle vertical asymptotes and potential division by zero.
    # We will split the curve into segments separated by asymptotes.
    epsilon = 1e-3 # Small value to identify points near zero (for asymptotes)
    
    segments_1_over_f = []
    current_segment_x = []
    current_segment_y = []

    for i in range(len(x_vals)): # Iterate through x values
        x_val = x_vals[i]
        y_val = y_vals[i]

        if abs(y_val) < epsilon: # If f(x) is close to zero, it's an asymptote
            if current_segment_x: # If there's an active segment, save it
                segments_1_over_f.append((current_segment_x, current_segment_y))
            current_segment_x = [] # Start a new segment after the asymptote
            current_segment_y = []
        else:
            current_segment_x.append(x_val)
            current_segment_y.append(1 / y_val)
    
    # Add the last segment if any data remains
    if current_segment_x:
        segments_1_over_f.append((current_segment_x, current_segment_y))

    # Plot each segment of y = 1/f(x)
    for idx, (seg_x, seg_y) in enumerate(segments_1_over_f):
        # Only show legend for the first segment to avoid multiple legend entries
        fig.add_trace(go.Scatter(x=seg_x, y=seg_y, mode='lines', name='y = 1/f(x)' if idx == 0 else '', line=dict(color='green', width=2), showlegend=(idx == 0)))
    
    # Add explicit vertical asymptote lines for clarity
    fig.add_trace(go.Scatter(x=[1, 1], y=[-10, 10], mode='lines', name='VA at x=1', line=dict(color='red', dash='dash', width=1), showlegend=False))
    fig.add_trace(go.Scatter(x=[3, 3], y=[-10, 10], mode='lines', name='VA at x=3', line=dict(color='red', dash='dash', width=1), showlegend=False))
    
    # --- Add Key Points for Clarity (Optional, but good for explanation) --- 
    # These markers highlight specific characteristic points on the graphs.
    
    # For original f(x)
    fig.add_trace(go.Scatter(x=x_key_points, y=y_key_points, mode='markers', name='Key points f(x)',
                             marker=dict(color='black', size=6, symbol='circle'), showlegend=False))
    
    # For y = f(|x|)
    # Points: reflected x-intercepts, y-intercept, reflected local minimum
    f_abs_x_specific_points = np.array([-3, -1, 0, 1, 2, 3, -2]) 
    f_abs_y_specific_points = np.array([0, 0, 2, 0, -0.67, 0, -0.67])
    fig.add_trace(go.Scatter(x=f_abs_x_specific_points, y=f_abs_y_specific_points, mode='markers', name='Key points f(|x|)',
                             marker=dict(color='blue', size=6, symbol='square'), showlegend=False))

    # For y = 1/f(x)
    # Points: y-intercept, transformed local minimum
    reciprocal_x_specific_points = np.array([0, 2])
    reciprocal_y_specific_points = np.array([1/2, 1/(-0.67)])
    fig.add_trace(go.Scatter(x=reciprocal_x_specific_points, y=reciprocal_y_specific_points, mode='markers', name='Key points 1/f(x)',
                             marker=dict(color='green', size=6, symbol='diamond'), showlegend=False))

    # --- Layout Settings for the Plotly Figure ---
    fig.update_layout(
        title='HSC Graph Transformations (y = f(|x|) and y = 1/f(x))',
        xaxis_title='x',
        yaxis_title='y',
        xaxis_range=[-4.5, 4.5], # Slightly wider range for better visualization
        yaxis_range=[-5, 5],     # Adjust range to show asymptotes and behavior clearly
        showlegend=True,
        legend=dict(x=0.01, y=0.99, bgcolor='rgba(255,255,255,0.8)', bordercolor='rgba(0,0,0,0.5)', borderwidth=1),
        hovermode='x unified', # Good for interactive exploration
        height=600,
        width=800,
        template="plotly_white" # Clean white background
    )
    # Add gridlines and zero lines for a clearer graph
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray', zeroline=True, zerolinewidth=2, zerolinecolor='black', tickvals=np.arange(-4, 5, 1))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray', zeroline=True, zerolinewidth=2, zerolinecolor='black', tickvals=np.arange(-5, 6, 1))

    return fig