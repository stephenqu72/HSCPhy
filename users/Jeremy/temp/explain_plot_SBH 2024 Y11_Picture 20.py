import plotly.graph_objects as go
import numpy as np

def generate_plot():
    path_difference = 2.0  # meters

    # Combine all wavelengths from the options to check them
    possible_lambdas_to_check = [
        1.0, 3.0, 5.0,  # Option A
        1.3, 2.0, 4.0,  # Option B
        0.5, 1.5, 2.5,  # Option C
        0.8, 1.3, 4.0   # Option D
    ]
    
    # Remove duplicates and sort for cleaner processing
    possible_lambdas_to_check = sorted(list(set(possible_lambdas_to_check)))

    valid_lambdas = []
    corresponding_n_values = []
    
    # Check each potential wavelength against the destructive interference condition
    # For destructive interference: PD = (n + 0.5) * lambda
    # Rearranging for n: n = (PD / lambda) - 0.5
    for l in possible_lambdas_to_check:
        n_float = (path_difference / l) - 0.5
        
        # Check if n_float is very close to a non-negative integer
        # Use a small tolerance for floating point comparisons (e.g., 0.01)
        if abs(n_float - round(n_float)) < 0.01 and round(n_float) >= 0:
            valid_lambdas.append(l)
            corresponding_n_values.append(int(round(n_float))) # Store as integer
            
    fig = go.Figure()

    # Plot the wavelengths that satisfy the destructive interference condition
    fig.add_trace(go.Scatter(
        x=[f'{l} m' for l in valid_lambdas],
        y=[1] * len(valid_lambdas), # Dummy y-value to indicate presence
        mode='markers',
        marker=dict(size=15, symbol='star', color='darkgreen'),
        name='Valid Wavelengths for Destructive Interference'
    ))

    # Add annotations for the 'n' value associated with each valid wavelength
    for i, l in enumerate(valid_lambdas):
        fig.add_annotation(
            x=f'{l} m',
            y=1,
            text=f'n={corresponding_n_values[i]}',
            showarrow=True,
            arrowhead=1,
            yshift=15,
            font=dict(color='darkgreen')
        )

    fig.update_layout(
        title='Wavelengths from Options Causing Destructive Interference (PD=2.0m)',
        xaxis_title='Wavelength (m)',
        yaxis_title='Condition Met',
        yaxis_tickvals=[1],
        yaxis_ticktext=['Destructive Interference'],
        yaxis_range=[0.5, 1.5],
        height=450,
        showlegend=False,
        template='plotly_white'
    )
    
    return fig