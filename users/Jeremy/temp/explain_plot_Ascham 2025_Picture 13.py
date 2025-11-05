import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def generate_plot():
    x = np.linspace(-4.5, 4.5, 500)
    f_x = x**2 - 4
    abs_f_x = np.abs(f_x)

    # For 1/|f(x)|, handle asymptotes
    # Create a finer x for reciprocal, and replace inf with nan
    x_reciprocal = np.linspace(-4.5, 4.5, 1000)
    f_x_reciprocal = x_reciprocal**2 - 4
    abs_f_x_reciprocal = np.abs(f_x_reciprocal)
    
    # Avoid division by zero by setting values very close to zero to NaN
    y_reciprocal = np.where(abs_f_x_reciprocal < 1e-3, np.nan, 1 / abs_f_x_reciprocal)
    
    fig = make_subplots(rows=1, cols=2, subplot_titles=(r'$y = |x^2 - 4|$', r'$y = \frac{1}{|x^2 - 4|}$'))

    # Subplot 1: y = |f(x)|
    fig.add_trace(go.Scatter(x=x, y=f_x, mode='lines', name='$f(x) = x^2 - 4$', 
                             line=dict(dash='dash', color='grey')), 
                  row=1, col=1)
    fig.add_trace(go.Scatter(x=x, y=abs_f_x, mode='lines', name='$y = |f(x)|$', 
                             line=dict(color='blue')), 
                  row=1, col=1)
    fig.add_trace(go.Scatter(x=[-2, 2], y=[0, 0], mode='markers', name='x-intercepts', 
                             marker=dict(color='red', size=8), showlegend=False), 
                  row=1, col=1)
    fig.add_trace(go.Scatter(x=[0], y=[4], mode='markers', name='vertex', 
                             marker=dict(color='red', size=8), showlegend=False), 
                  row=1, col=1)
    fig.update_xaxes(range=[-4.5, 4.5], title_text="x", row=1, col=1)
    fig.update_yaxes(range=[-5, 5], title_text="y", row=1, col=1)
    fig.update_layout(xaxis1_tickvals=[-4, -2, 0, 2, 4], yaxis1_tickvals=[-4, -2, 0, 2, 4])
    fig.update_layout(height=500, width=1000, title_text="Graph Sketches for Question 11(e)")

    # Subplot 2: y = 1/|f(x)|
    fig.add_trace(go.Scatter(x=x_reciprocal, y=y_reciprocal, mode='lines', name='$y = \frac{1}{|f(x)|}$', 
                             line=dict(color='red')), 
                  row=1, col=2)
    # Add vertical asymptotes
    fig.add_vline(x=-2, line_dash="dash", line_color="grey", row=1, col=2)
    fig.add_vline(x=2, line_dash="dash", line_color="grey", row=1, col=2)
    # Add horizontal asymptote
    fig.add_hline(y=0, line_dash="dash", line_color="grey", row=1, col=2)
    fig.add_trace(go.Scatter(x=[0], y=[0.25], mode='markers', name='local minimum', 
                             marker=dict(color='red', size=8), showlegend=False), 
                  row=1, col=2)
    fig.update_xaxes(range=[-4.5, 4.5], title_text="x", row=1, col=2)
    fig.update_yaxes(range=[-0.5, 6], title_text="y", row=1, col=2)
    fig.update_layout(xaxis2_tickvals=[-4, -2, 0, 2, 4], yaxis2_tickvals=[0, 0.25, 1, 2, 4, 6])

    fig.update_layout(showlegend=True)
    return fig