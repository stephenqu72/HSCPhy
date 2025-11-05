import plotly.graph_objects as go
import numpy as np
import math

def generate_plot():
    # Example values for a and b (can be varied to test different quadrants)
    # Let's use a=1, b=sqrt(3) (phi in Q1)
    a = 1
    b = np.sqrt(3)
    
    # Uncomment for a different quadrant example:
    # a = -1
    # b = 1 # phi in Q2

    # a = -1
    # b = -1 # phi in Q3
    
    # a = 1
    # b = -1 # phi in Q4
    
    R = np.sqrt(a**2 + b**2)

    # Define phi such that cos(phi) = a/R and sin(phi) = b/R
    # np.arctan2(y, x) gives angle in (-pi, pi]
    phi = np.arctan2(b, a)
    if phi <= 0:
        phi += 2 * np.pi # Adjust to (0, 2pi) range as per problem's angle constraints for delta
    
    # Calculate angles based on phi, ensuring they are in (0, 2pi)
    # 1. For R sin(x + alpha): cos(alpha) = b/R, sin(alpha) = a/R
    # This means alpha is related to (pi/2 - phi)
    alpha_raw = np.pi/2 - phi
    alpha = alpha_raw
    if alpha <= 0:
        alpha += 2 * np.pi
    elif alpha >= 2 * np.pi:
        alpha -= 2 * np.pi
    
    # 2. For R sin(x - beta): cos(beta) = b/R, sin(beta) = -a/R
    # This means beta is related to (-pi/2 + phi)
    beta_raw = -np.pi/2 + phi
    beta = beta_raw
    if beta <= 0:
        beta += 2 * np.pi
    elif beta >= 2 * np.pi:
        beta -= 2 * np.pi

    # 3. For R cos(x + gamma): cos(gamma) = a/R, sin(gamma) = -b/R
    # This means gamma is related to (-phi)
    gamma_raw = -phi
    gamma = gamma_raw
    if gamma <= 0:
        gamma += 2 * np.pi
    elif gamma >= 2 * np.pi:
        gamma -= 2 * np.pi

    # 4. For R cos(x - delta): cos(delta) = a/R, sin(delta) = b/R
    # This means delta is phi itself
    delta = phi

    angles_rad = [alpha, beta, gamma, delta]
    labels = ['alpha', 'beta', 'gamma', 'delta']
    
    # Create unit circle
    t = np.linspace(0, 2 * np.pi, 100)
    x_circle = np.cos(t)
    y_circle = np.sin(t)

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=x_circle, y=y_circle, mode='lines', name='Unit Circle', 
                             line=dict(color='lightgrey', width=1)))

    # Add origin and axes
    fig.add_shape(type="line", x0=-1.1, y0=0, x1=1.1, y1=0, line=dict(color="black", width=1))
    fig.add_shape(type="line", x0=0, y0=-1.1, x1=0, y1=1.1, line=dict(color="black", width=1))
    fig.add_annotation(x=1.05, y=0, text="x", showarrow=False, yshift=10)
    fig.add_annotation(x=0, y=1.05, text="y", showarrow=False, xshift=10)

    # Add points and angles
    for i, angle_val in enumerate(angles_rad):
        # Determine coordinates on the unit circle based on the definition for each angle
        x_coord, y_coord = 0, 0
        if labels[i] == 'delta':  # cos(delta) = a/R, sin(delta) = b/R
            x_coord, y_coord = a/R, b/R
        elif labels[i] == 'alpha': # cos(alpha) = b/R, sin(alpha) = a/R
            x_coord, y_coord = b/R, a/R
        elif labels[i] == 'beta':  # cos(beta) = b/R, sin(beta) = -a/R
            x_coord, y_coord = b/R, -a/R
        elif labels[i] == 'gamma': # cos(gamma) = a/R, sin(gamma) = -b/R
            x_coord, y_coord = a/R, -b/R
        
        # Add a point for each angle's (cos, sin) on the unit circle
        fig.add_trace(go.Scatter(x=[x_coord], y=[y_coord], mode='markers',
                                 marker=dict(size=10, color=['red', 'green', 'blue', 'purple'][i]),
                                 name=f'{labels[i]} ({np.degrees(angle_val):.0f}°)' ))
        
        # Add annotation for the angle label
        fig.add_annotation(x=x_coord * 1.15, y=y_coord * 1.15,
                           text=f'{labels[i]}', showarrow=False, font=dict(color=['red', 'green', 'blue', 'purple'][i]))

        # Add an arc for delta (phi) for better visualization of the reference angle
        if labels[i] == "delta":
            theta_arc = np.linspace(0, angle_val, 50)
            fig.add_trace(go.Scatter(x=0.2 * np.cos(theta_arc), y=0.2 * np.sin(theta_arc),
                                     mode='lines', line=dict(color='orange', width=2), name='phi arc'))
            fig.add_annotation(x=0.3 * np.cos(angle_val/2), y=0.3 * np.sin(angle_val/2),
                               text=f'phi', showarrow=False, font=dict(color='orange'))

    fig.update_layout(title=f'Auxiliary Angle Forms on Unit Circle (a={a:.2f}, b={b:.2f})', # Added .2f for cleaner display
                      xaxis_title="cos(angle)",
                      yaxis_title="sin(angle)",
                      xaxis=dict(range=[-1.2, 1.2], showgrid=False, zeroline=False, scaleanchor="y", scaleratio=1),
                      yaxis=dict(range=[-1.2, 1.2], showgrid=False, zeroline=False),
                      showlegend=True,
                      hovermode="closest",
                      height=600, width=600)
    
    return fig