import plotly.graph_objects as go
import numpy as np
from scipy.stats import norm

def generate_plot():
    # Define parameters for the standard normal distribution
    mu = 0
    sigma = 1
    
    # Generate x values
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 500)
    
    # Calculate PDF values
    pdf = norm.pdf(x, mu, sigma)
    
    # Create the plot
    fig = go.Figure()
    
    # Add the normal distribution curve
    fig.add_trace(go.Scatter(x=x, y=pdf, mode='lines', name='Standard Normal Distribution',
                             line=dict(color='blue')))
    
    # Highlight the area for Z <= -0.62
    z_value = -0.62
    x_shade = np.linspace(mu - 4*sigma, z_value, 200)
    pdf_shade = norm.pdf(x_shade, mu, sigma)
    fig.add_trace(go.Scatter(x=x_shade, y=pdf_shade, fill='tozeroy', mode='none',
                             fillcolor='rgba(255, 0, 0, 0.3)', name=f'P(Z <= {z_value})'))
    
    # Add a vertical line for z_value
    fig.add_vline(x=z_value, line_dash="dash", line_color="red", annotation_text=f"Z = {z_value}", annotation_position="top left")
    
    # Add a vertical line for the mean
    fig.add_vline(x=mu, line_dash="dash", line_color="green", annotation_text=f"Mean = {mu}", annotation_position="top right")

    # Update layout
    fig.update_layout(title='Standard Normal Distribution: P(Z &le; -0.62)',
                      xaxis_title='Z-score',
                      yaxis_title='Probability Density',
                      hovermode='x unified',
                      showlegend=True)
    
    return fig