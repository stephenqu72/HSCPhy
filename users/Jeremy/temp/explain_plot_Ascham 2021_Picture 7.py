import plotly.graph_objects as go
import numpy as np

def generate_plot():
    p = 0.64 # True population proportion
    n = 50 # Sample size for each individual sample
    k_initial = 20 # Initial number of samples
    k_final = 25 # Number of samples after adding 5 more

    # Range of K values for the plot
    K_values = np.arange(1, 51, 1) # From 1 to 50 for good visualization

    # Calculate sigma_p_bar for each K
    # Formula: sigma_p_bar = sqrt(p * (1-p) / (n * K))
    sigma_p_bar_values = np.sqrt((p * (1 - p)) / (n * K_values))

    # Calculate specific values for K=20 and K=25
    sigma_k_initial = np.sqrt((p * (1 - p)) / (n * k_initial))
    sigma_k_final = np.sqrt((p * (1 - p)) / (n * k_final))

    fig = go.Figure()

    # Main line plot for standard error
    fig.add_trace(go.Scatter(x=K_values, y=sigma_p_bar_values, mode='lines',
                             name='Standard Error of Mean Sample Proportion (σ<sub>p&#770;</sub>)',
                             line=dict(color='blue', width=2)))

    # Mark initial point (K=20)
    fig.add_trace(go.Scatter(x=[k_initial], y=[sigma_k_initial],
                             mode='markers',
                             marker=dict(size=10, color='red', symbol='circle'),
                             name=f'Initial (K={k_initial})<br>σ<sub>p&#770;</sub>={sigma_k_initial:.4f}'))
    # Line for initial point
    fig.add_trace(go.Scatter(x=[k_initial, k_initial], y=[0, sigma_k_initial],
                             mode='lines',
                             line=dict(dash='dot', color='red', width=1),
                             showlegend=False))

    # Mark final point (K=25)
    fig.add_trace(go.Scatter(x=[k_final], y=[sigma_k_final],
                             mode='markers',
                             marker=dict(size=10, color='green', symbol='circle'),
                             name=f'New (K={k_final})<br>σ<sub>p&#770;</sub>={sigma_k_final:.4f}'))
    # Line for final point
    fig.add_trace(go.Scatter(x=[k_final, k_final], y=[0, sigma_k_final],
                             mode='lines',
                             line=dict(dash='dot', color='green', width=1),
                             showlegend=False))

    fig.update_layout(
        title='Impact of Number of Samples (K) on Standard Error of Mean Sample Proportion',
        xaxis_title='Number of Samples (K)',
        yaxis_title='Standard Error (σ<sub>p&#770;</sub>)',
        hovermode='x unified',
        template='plotly_white',
        legend=dict(x=0.01, y=0.99, bgcolor='rgba(255,255,255,0.8)')
    )
    return fig