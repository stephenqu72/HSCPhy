import plotly.graph_objects as go
import numpy as np
import base64
import json

def generate_plot():
    # Key points from the graph (t, v)
    t_freefall_curve = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    v_freefall_curve = np.array([0, -18, -30, -39, -45, -50, -55, -57, -59, -59]) # More detailed points for a smoother curve

    # Parachute opening section (9 to 11 seconds) - linear
    t_parachute_opening = np.array([9, 10, 11])
    v_parachute_opening = np.array([-59, -35, -15]) # Including a point at t=10 for better representation

    # Gliding section (11 to 13 seconds and beyond) - constant velocity
    t_gliding = np.array([11, 13])
    v_gliding = np.array([-15, -15])

    fig = go.Figure()

    # Plot freefall section
    fig.add_trace(go.Scatter(x=t_freefall_curve, y=v_freefall_curve, mode='lines', name='Freefall', line=dict(color='blue', width=2)))
    # Plot parachute opening section
    fig.add_trace(go.Scatter(x=t_parachute_opening, y=v_parachute_opening, mode='lines', name='Parachute Opening', line=dict(color='green', width=2)))
    # Plot gliding section
    fig.add_trace(go.Scatter(x=t_gliding, y=v_gliding, mode='lines', name='Gliding', line=dict(color='red', width=2)))

    # Shading for part (a) - Area under freefall curve (0 to 9 seconds)
    t_area = np.concatenate([t_freefall_curve, np.flip(t_freefall_curve)])
    v_area = np.concatenate([v_freefall_curve, np.zeros_like(v_freefall_curve)])
    fig.add_trace(go.Scatter(x=t_area, y=v_area, fill='toself', fillcolor='rgba(0,0,255,0.1)', line=dict(width=0), name='Area for (a)'))

    # Mark points for part (b) calculation (acceleration)
    fig.add_trace(go.Scatter(x=[9, 11], y=[-59, -15], mode='markers', name='Points for Accel (b)', marker=dict(color='orange', size=8, line=dict(width=1, color='DarkSlateGrey'))))
    
    # Mark point for part (c) (terminal velocity)
    fig.add_trace(go.Scatter(x=[9], y=[-59], mode='markers', name='Terminal Velocity for (c)', marker=dict(color='purple', size=8, line=dict(width=1, color='DarkSlateGrey'))))

    fig.update_layout(
        title='Velocity vs Time for a Skydiver Journey', # Updated title for clarity
        xaxis_title='Time (seconds)',
        yaxis_title='Velocity (ms⁻¹)',
        xaxis=dict(range=[-0.5, 13.5], dtick=2, tick0=0, showgrid=True, gridcolor='lightgray'), # Show grid
        yaxis=dict(range=[-80, 5], dtick=20, showgrid=True, gridcolor='lightgray'),
        hovermode="x unified",
        margin=dict(l=50, r=50, t=50, b=50)
    )
    
    # Add annotations for the sections
    fig.add_annotation(
        x=4.5, y=2,
        text="Free falling",
        showarrow=False,
        font=dict(size=12, color="blue"),
    )
    fig.add_annotation(
        x=10, y=2,
        text="Parachute opening",
        showarrow=False,
        font=dict(size=12, color="green"),
    )
    fig.add_annotation(
        x=12.5, y=2,
        text="Gliding",
        showarrow=False,
        font=dict(size=12, color="red"),
    )
    return fig